from pwn import *
from tqdm import tqdm
from string import printable

flag_len = 32

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

encrypted = ""
for c in key:
    encrypted += encode_char('a', str.encode(c))[0]
print(f"Key is valid: {dummy_encrypted == encrypted}")

