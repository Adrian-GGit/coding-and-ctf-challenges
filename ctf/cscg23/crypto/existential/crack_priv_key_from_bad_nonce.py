import ecdsa
import os
import random
import libnum
import hashlib
from hashlib import shake_128
import olll
from ecdsa.util import string_to_number
from ecdsa._compat import normalise_bytes

def efficient_k(msg):
    return int.from_bytes(
        shake_128(msg).digest(16) + os.urandom(16),
        "big"
    )

curve = ecdsa.curves.BRAINPOOLP256r1
gen = curve.generator
order = gen.order()

signing_key = ecdsa.SigningKey.generate(curve=ecdsa.curves.BRAINPOOLP256r1)
priv_key = signing_key.privkey
verifying_key = signing_key.get_verifying_key()
pub_key = verifying_key.pubkey

hex_message1 = bytes.fromhex("41")
hex_message2 = bytes.fromhex("42")
msg1 = string_to_number(normalise_bytes(hashlib.sha1(hex_message1).digest()))
msg2 = string_to_number(normalise_bytes(hashlib.sha1(hex_message2).digest()))

# TODO: change these to using efficient_k
nonce1 = efficient_k(hex_message1)
nonce2 = efficient_k(hex_message2)
print(f"nonce1: {nonce1}, nonce2: {nonce2}")
# nonce1 = random.randrange(1, 2**127)
# nonce2 = random.randrange(1, 2**127)
# print(f"nonce1: {nonce1}, nonce2: {nonce2}, 2**127: {2**127}")
nonce_range = 2**128

sig1 = priv_key.sign(msg1, nonce1)
sig2 = priv_key.sign(msg2, nonce2)

r1 = sig1.r
s1_inv = libnum.invmod(sig1.s, order)
r2 = sig2.r
s2_inv = libnum.invmod(sig2.s, order)

matrix = [
	[order, 0, 0, 0],
	[0, order, 0, 0],
	[r1*s1_inv, r2*s2_inv, (nonce_range) / order, 0],
	[msg1*s1_inv, msg2*s2_inv, 0, nonce_range]
]
new_matrix = olll.reduction(matrix, 0.75)
r1_inv = libnum.invmod(sig1.r, order)
s1 = sig1.s

for row in new_matrix:
	potential_nonce_1 = row[0]
	potential_priv_key = r1_inv * ((potential_nonce_1 * s1) - msg1)
	if ecdsa.ecdsa.Public_key(gen, gen * potential_priv_key) == pub_key:
		print("found private key!")