from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 1000

r = remote("mercury.picoctf.net", 41934)
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
bin_flag = unhex(flag)

counter = KEY_LEN - len(bin_flag)

while counter > 0:
    chunk_size = min(MAX_CHUNK, counter)
    r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
    counter -= chunk_size

r.sendlineafter("What data would you like to encrypt? ", bin_flag)
r.recvlineS()
log.success("The flag: {}".format(unhex(r.recvlineS())))
