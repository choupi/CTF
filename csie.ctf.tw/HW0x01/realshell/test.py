import socket
import sys

def readuntil(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('csie.ctf.tw', 6010))
f = s.makefile('rw', bufsize=0)

print readuntil(f, ':')
p=open(sys.argv[1])
pp=p.read(100)
print pp
f.write(pp+'\n')
print f.read(100)
