import os
import ecdsa
import binascii
import hashlib
from hashlib import shake_128
from ecdsa._compat import normalise_bytes
from ecdsa.keys import _truncate_and_convert_digest
from ecdsa.util import sigencode_string, sigencode_strings, string_to_number, bit_length
from ecdsa.ecdsa import Signature, digest_integer
import libnum
import olll


class KeyCracker:
	def __init__(self, messages=[], message_digests=[], signatures=[]):
		self.messages = messages
		self.message_digests = message_digests
		self.signatures = signatures
		self.curve = ecdsa.curves.BRAINPOOLP256r1
		self.generator = self.curve.generator
		self.public_key = None

	def init_test(self, message="41"):
		self.test_message = bytes.fromhex(message) # 66 6C 61 67 => "flag"
		self.test_signing_key = ecdsa.SigningKey.generate(curve=self.curve)
		self.test_verifying_key = self.test_signing_key.get_verifying_key()
		self.test_private_key = self.test_signing_key.privkey
		self.test_public_key = self.test_verifying_key.pubkey
		self.test_digest = normalise_bytes(self.test_signing_key.default_hashfunc(self.test_message).digest())
		self.test_message_digest = string_to_number(self.test_digest)
		self.test_num = _truncate_and_convert_digest(self.test_digest, self.curve, True)
		self.test_r, self.test_s = self.test_signing_key.sign_number(self.test_num, None, self.efficient_k(self.test_message))
		self.test_sig = sigencode_string(self.test_r, self.test_s, self.curve.order).hex()

	def get_r_s_from_signature(self, signature_hash):
		return int(signature_hash[:64], 16), int(signature_hash[64:], 16)

	def efficient_k(self, msg):
	    return int.from_bytes(
	        shake_128(msg).digest(16) + os.urandom(16),
	        "big"
	    )

	def get_public_key(self):
		public_keys = []
		for message_digest, signature_hash in zip(self.message_digests, self.signatures):
			r, s = self.get_r_s_from_signature(signature_hash)
			signature = Signature(r, s)
			pub_1, pub_2 = signature.recover_public_keys(message_digest, self.generator)
			for pub_key in public_keys:
				for calced_pub_key in [pub_1, pub_2]:
					if pub_key == calced_pub_key:
						self.public_key = pub_key
						break
			public_keys.extend([pub_1, pub_2])

	def get_private_key_from_k(self, k, r_inv, s, message_digest):
		return (r_inv * ((k * s) - message_digest)) % self.curve.order

	def brute_force_private_key(self, r1, r_inv, s1, s1_inv, r2, r2_inv, s2, s2_inv, message1, message2):
		matrix = [
			[self.curve.order, 0, 0, 0],
			[0, self.curve.order, 0, 0],
			[r1*s1_inv, r2*s2_inv, (2**128) / self.curve.order, 0],
			[int.from_bytes(message1, byteorder="big")*s1_inv, int.from_bytes(message2, byteorder="big")*s2_inv, 0, 2**128]
		]
		new_matrix = olll.reduction(matrix, 0.75)

		for row in new_matrix:
			k = row[0]
			potential_private_key = (r_inv * ((k * s1) - int.from_bytes(message1, byteorder="big"))) % self.curve.order
			if self.generator * potential_private_key == self.test_public_key.point: # self.public_key.point:
				self.private_key = ecdsa.ecdsa.Private_key(self.public_key, potential_private_key)
				print("[*] Cracked private key")

first_message = bytes.fromhex("41")
second_message = bytes.fromhex("42")
signatures = [
	"02c5d879b7a65684b53f6f9cbfcdeac3cb484af025c76d132bd2a6e355dbe6410af3a9d7dbf2777c2e34f1b9632ebb0a200d776844444f76df0bea4b0613731d",
	"176e8d6e8653cef1d0cabe7cb5ffe78ec5f80c60c30e507df1c9e5811c8fe7bf24705b836d30a568c9632aa390a533044a7fa8e94ff1baed7c6d94710720ef18"
]
messages = [first_message, second_message]
message_digests = [
	string_to_number(normalise_bytes(hashlib.sha1(first_message).digest())),
	string_to_number(normalise_bytes(hashlib.sha1(second_message).digest()))
]
cracker = KeyCracker(messages, message_digests, signatures)
cracker.get_public_key()

cracker.init_test("41")
k = cracker.efficient_k(cracker.test_message)
r1, s1 = cracker.get_r_s_from_signature(cracker.test_sig)
m1 = cracker.test_message_digest
got_private_key = cracker.get_private_key_from_k(k, libnum.invmod(r1, cracker.curve.order), s1, cracker.test_message_digest)
print(got_private_key)
cracker.init_test("42")
r2, s2 = cracker.get_r_s_from_signature(cracker.test_sig)
m2 = cracker.test_message_digest
print(f"k: {k}")
cracker.brute_force_private_key(
	r1, libnum.invmod(r1, cracker.curve.order), s1, libnum.invmod(s1, cracker.curve.order),
	r2, libnum.invmod(r2, cracker.curve.order), s2, libnum.invmod(s2, cracker.curve.order),
	first_message,
	second_message,
)
print(cracker.test_private_key)
print(cracker.private_key)