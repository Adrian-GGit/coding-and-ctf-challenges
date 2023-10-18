from pwn import *
from tqdm import tqdm
from string import printable

flag_len = 32

# key_len = 50000
# r = remote("mercury.picoctf.net", 41934)
# to_encode = "a" * (key_len - flag_len)
# r.sendlineafter("What data would you like to encrypt? ", to_encode)
# dummy = "a" * (flag_len)
# # dummy = "abaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# r.sendlineafter("What data would you like to encrypt? ", dummy)
# out = r.recvlines(2)
# dummy_encrypted = out[1].decode("utf-8")
# print(f"[*] Encoded: {dummy_encrypted}")

dummy_encrypted = "0346303d1902033d1959003d1903553d1951553d1907593d1951511a3d190505"

def encode_char(c, k):
    return list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), c, k))

key = ""
for i in tqdm(range(0, len(dummy_encrypted), 2)):
    for k in printable:
        encoded = encode_char('a', str.encode(k))[0]
        compare = dummy_encrypted[i:i + 2]
        if encoded == compare:
            key += k
            print(f"[*] Building key: {key}")
            break
print(f"[*] Brute forced key: {key}")

# validate
encrypted = ""
for c in key:
    encrypted += encode_char('a', str.encode(c))[0]
print(f"Key is valid: {dummy_encrypted == encrypted}")

