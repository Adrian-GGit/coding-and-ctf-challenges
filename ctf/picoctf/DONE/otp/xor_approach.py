# main mistake bei brute force methode:
# in python stellt "^" nicht a hoch b dar als mathematische Operation
# sondern den einfachen xor Operator
# xor ist reversable während "hoch" nicht ohne weiteres umgekehrt werden kann
# der hauptgedanke bei dem brute force approach war dass die Operation nicht reversierbar ist
# was sie aber offensichtlich ist weil "^" nicht der "hoch" Operator ist sondern schlichtweg XOR
# => merken was "^" macht!!!

from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 1000

r = remote("mercury.picoctf.net", 41934)
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
log.info(f"Flag: {flag}")
bin_flag = unhex(flag)

counter = KEY_LEN - len(bin_flag)

with log.progress('Causing wrap-around') as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(MAX_CHUNK, counter)
        r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        
        counter -= chunk_size

r.sendlineafter("What data would you like to encrypt? ", bin_flag)
r.recvlineS()
log.success("The flag: {}".format(unhex(r.recvlineS())))
