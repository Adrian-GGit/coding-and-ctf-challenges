from string import printable

from tqdm import tqdm

pwned_key = "b'Q\\xcb\\x8a\\xb4\\x04\\xf8\\x00{\\xdd"
encrypted_flag = "0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d"
flag = b""

def encode_char(c, i):
    return list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), c, str.encode(pwned_key[i])))

for i in tqdm(range(len(pwned_key))):
    for c in printable:
        encoded = encode_char(c, i)[0]
        compare = encrypted_flag[i*2:i*2 + 2]
        print((c, encoded, compare))
        if encoded == compare:
            flag += str.encode(c)
            print(f"[*] Building flag: {i, flag}")
            break
print(f"[*] Brute forced flag: {flag}")
