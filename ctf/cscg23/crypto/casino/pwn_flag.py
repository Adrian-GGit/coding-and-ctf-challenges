from pwn import *

GUESS = 'Guess the random bit I have coosen!'

r = remote("9be2e21c4b80c58328397e4d-casino.challenge.master.cscg.live", 31337)
# r.recvuntil(GUESS)
print(r.recvliineS(keepends = False))

# flag = r.recvlineS(keepends = False)
# log.info(f"Flag: {flag}")
# bin_flag = unhex(flag)

# counter = KEY_LEN - len(bin_flag)

# with log.progress('Causing wrap-around') as p:
#     while counter > 0:
#         p.status(f"{counter} bytes left")
#         chunk_size = min(MAX_CHUNK, counter)
#         r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        
#         counter -= chunk_size

# r.sendlineafter("What data would you like to encrypt? ", bin_flag)
# r.recvlineS()
# log.success("The flag: {}".format(unhex(r.recvlineS())))
