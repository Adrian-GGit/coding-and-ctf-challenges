import ecdsa
import os
import random
import libnum
import hashlib
from hashlib import shake_128
import olll
from ecdsa.util import string_to_number, sigencode_string
from ecdsa._compat import normalise_bytes
from ecdsa.ecdsa import Signature

def efficient_k(msg):
    return int.from_bytes(
        shake_128(msg).digest(16) + os.urandom(16),
        "big"
    )

def get_public_key(gen, messages, signatures):
    public_keys = []
    for message, signature in zip(messages, signatures):
        pub_1, pub_2 = signature.recover_public_keys(message, gen)
        for pub_key in public_keys:
            for calced_pub_key in [pub_1, pub_2]:
                if pub_key == calced_pub_key:
                    return pub_key
        public_keys.extend([pub_1, pub_2])

def get_r_s_from_signature(signature_hash):
    return int(signature_hash[:64], 16), int(signature_hash[64:], 16)

def sig_hex_to_sig(sig_hash):
    r, s = get_r_s_from_signature(sig_hash)
    return Signature(r, s)

curve = ecdsa.curves.BRAINPOOLP256r1
gen = curve.generator
order = gen.order()

signing_key = ecdsa.SigningKey.generate(curve=ecdsa.curves.BRAINPOOLP256r1)
priv_key = signing_key.privkey
verifying_key = signing_key.get_verifying_key()
pub_key = verifying_key.pubkey

similar_bits_range = 2**128
needed_signatures = 6
# yubikey_fixed_prefix = random.randrange(similar_bits_range, order)
# hex_msgs = [bytes.fromhex(str(40 + i)) for i in range(needed_signatures)]
hex_msgs = [bytes.fromhex(str(40)) for i in range(needed_signatures)]
msgs = [string_to_number(normalise_bytes(hashlib.sha1(hex_msgs[i]).digest())) for i in range(needed_signatures)]
# nonces = [random.randrange(1, similar_bits_range) + yubikey_fixed_prefix for i in range(needed_signatures)]
nonces = [efficient_k(hex_msgs[i]) for i in range(needed_signatures)]
# sigs = [priv_key.sign(msgs[i], nonces[i]) for i in range(needed_signatures)]
sigs = [
    sig_hex_to_sig("0ff956db39eb35926ea60997879846820831e08e766f15c8b45d72d5e569bdd97a8c57cf709c23ad935bfa3798f9442308bcae766b9e12a747d2dec928f14fab"),
    sig_hex_to_sig("97c8aba2cd114e73cc1d6fb486d6f666b43c14cedd0e53705184131381d4f9ae3ff8081e34d0731adb2609f47853ddc229504e640a7072e70f8087477807a183"),
    sig_hex_to_sig("67bb99c8cbb4bfdbe14f414ddc866a952775f1efdb39c7376ea3b8d4a8765a9f9e92c6e58a96a0f1f12e0fc2d6270168133fae9b85b1dbb91af4ab3a3d5e3ad2"),
    sig_hex_to_sig("4b6a6ae76d25a8126d9cc2d3cf896ab7eff88214c0743d0a68002603222c118d8aa8b9a664821c732a8631cc7d9523e0e2bd0ce31430363aed66c79e88d0815a"),
    sig_hex_to_sig("32cd17d2267ce7f00d00aa389dec2388cc1e9e7bb4e2f3d79e2425eadd9151f45a15146c01fed4594a8d21265cbf13b127acd6ced27a9a2034f7761792fd512b"),
    sig_hex_to_sig("4e9f643a8067b3c69126ecf4254eeedec791ee9d7539946ddc0b1aee0f7d4a138e568a1fe08b925e8cabcba1ff9f76f3a42f48d81b86e97558d45c67e51e59c6"),
]
calced_pub_key = get_public_key(gen, msgs, sigs)

# print(nonces_from_efficient_k)
 
matrix = [
    [order, 0, 0, 0, 0, 0, 0],
    [0, order, 0, 0, 0, 0, 0],
    [0, 0, order, 0, 0, 0, 0],
    [0, 0, 0, order, 0, 0, 0],
    [0, 0, 0, 0, order, 0, 0]
]
 
row, row2 = [], []
[msgn, rn, sn] = [msgs[-1], sigs[-1].r, sigs[-1].s]
rnsn_inv = rn * libnum.invmod(sn, order)
mnsn_inv = msgn * libnum.invmod(sn, order)
 
# 2nd to last row: [r1(s1^-1) - rn(sn^-1), ... , rn-1(sn-1^-1) - rn(sn^-1), 2^176/order, 0 ]
# last row: [m1(s1^-1) - mn(sn^-1), ... , mn-1(sn-1^-1) - mn(sn^-1), 0, 2^176]
for i in range(needed_signatures - 1):
    row.append((sigs[i].r * libnum.invmod(sigs[i].s, order)) - rnsn_inv)
    row2.append((msgs[i] * libnum.invmod(sigs[i].s, order)) - mnsn_inv)
 
# add last elements of last two rows, B = 2**(256-80) for yubikey
row.append((similar_bits_range) / order)
row.append(0)
row2.append(0)
row2.append(similar_bits_range)
 
matrix.append(row)
matrix.append(row2)
 
new_matrix = olll.reduction(matrix, 0.75)
 
for row in new_matrix:
    potential_nonce_diff = row[0]

    # Secret key = (rns1 - r1sn)-1 (snm1 - s1mn - s1sn(k1 - kn))
    potential_priv_key = (sn * msgs[0]) - (sigs[0].s * msgn) - (sigs[0].s * sn * potential_nonce_diff)
    potential_priv_key *= libnum.invmod((rn * sigs[0].s) - (sigs[0].r * sn), order)

    # check if we found private key by comparing its public key with actual public key
    if ecdsa.ecdsa.Public_key(gen, gen * potential_priv_key) == calced_pub_key:
        print("Found private key!")
        calced_priv_key = ecdsa.ecdsa.Private_key(calced_pub_key, potential_priv_key)
        flag = bytes.fromhex("66 6C 61 67")
        flag_sig = calced_priv_key.sign(string_to_number(normalise_bytes(hashlib.sha1(flag).digest())), efficient_k(flag))
        print(f"Flag sign: {sigencode_string(flag_sig.r, flag_sig.s, order).hex()}")