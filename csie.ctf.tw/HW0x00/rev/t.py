import struct

ss='1234567890\n1'
s=[ord(i) for i in ss]
for i in [0,4]:
  s0=s[i]
  s1=s[i+1]
  s2=s[i+2]
  s3=s[i+3]
  s[i]=(s0^s1)^s2
  s[i+1]=s1^s3
  s[i+2]=s0^s2
  s[i+3]=s0^s1
  #z=int('%02x%02x%02x%02x'%(s[i+7],s[i+6],s[i+5],s[i+4]),16)
  #zz=int('%02x%02x%02x%02x'%(s[i+3],s[i+2],s[i+1],s[i]),16)
  #print z
  #print zz
  #z= (~z) & 0xffffffff
  #z=hex(z ^ zz)
  #print z
  s3=s[i]^s[i+1]^s[i+2]
  s1=s[i+1]^s3
  s0=s[i+3]^s1
  s2=s0^s1^s[i]
