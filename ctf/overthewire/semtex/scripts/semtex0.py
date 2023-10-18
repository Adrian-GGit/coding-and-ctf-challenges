import socket
import struct

HOSTRAW = "semtex.labs.overthewire.org"
HOSTIP = socket.gethostbyname(HOSTRAW)
PORT = 24000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOSTRAW, PORT))

executable = bytearray()
is_exec = True

while True:
    data = s.recv(1)
    if not data:
        break
    if is_exec:
        executable += data
        is_exec = False
    else:
        is_exec = True

executable.decode()
print(executable)
f = open("semtex0", "w")
f.write(executable)
f.close()
