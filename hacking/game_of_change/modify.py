import sys
import struct

with open(sys.argv[1], 'rb') as in_file:
    s=in_file.read(116)

#print len(s)
(u,c,h)=struct.unpack('<iii', s[:12])
ss=struct.pack('<iii', u,8000,10000)
s=ss+s[12:]
#print s
f=open(sys.argv[1], 'wb')
f.write(s)
f.close()
