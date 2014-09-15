import sys
import struct

f=open(sys.argv[1])
ff=f.read()
l=len(ff)
ss=ff[l-4:l]
out=''

i=0
s=[ord(x) for x in ff[l-4:l]]
s3=s[i]^s[i+1]^s[i+2]
s1=s[i+1]^s3
s0=s[i+3]^s1
s2=s0^s1^s[i]
print s0,s1,s2,s3
out='%c%c%c%c'%(chr(s0),chr(s1),chr(s2),chr(s3))+out
z=int('%02x%02x%02x%02x'%(s3,s2,s1,s0), 16)
z= (~z) & 0xffffffff
for ii in xrange(4,len(ff),4):
  s=[ord(x) for x in ff[l-ii-4:l-ii]]
  zz=int('%02x%02x%02x%02x'%(s[3],s[2],s[1],s[0]),16)
  zz=zz^z
  zz='%08x'%zz
  s=[int(zz[x:x+2],16) for x in xrange(0,len(zz),2)]
  s.reverse()
  s3=s[i]^s[i+1]^s[i+2]
  s1=s[i+1]^s3
  s0=s[i+3]^s1
  s2=s0^s1^s[i]
  print s0,s1,s2,s3
  out='%c%c%c%c'%(chr(s0),chr(s1),chr(s2),chr(s3))+out
  z=int('%02x%02x%02x%02x'%(s3,s2,s1,s0), 16)
  z= (~z) & 0xffffffff

print out

