import pwn
from usefulstuff import conversions
import rsa

server = "mercury.picoctf.net"
port = 28517
conn = pwn.remote(server, port)
for i in range(4):
    message = conn.recvline()

conn.recvuntil(b'n: ')
n = int(conversions.b_to_string(conn.recvline(b'n: ')))
conn.recvuntil(b'e: ')
e = int(conversions.b_to_string(conn.recvline()))
conn.recvuntil(b'ciphertext: ')
encrypted_flag = int(conversions.b_to_string(conn.recvline()))

encrypted_two = pow(2, e, n)
product = encrypted_flag * encrypted_two
conn.recvuntil(b'Give me ciphertext to decrypt:')
conn.send(product.to_bytes(length=len(str(product))))
print(f'conn recv: {conn.recvline()}')
print(conn.recvline())
