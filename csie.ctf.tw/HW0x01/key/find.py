import string
digs = string.digits + string.lowercase

def int2base(x, base):
  if x < 0: sign = -1
  elif x==0: return '0'
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

i=0
while True:
  ins=int2base(i, 4)
  if len(ins)>4: break
  while len(ins)<4: ins='0'+ins
  ins+='-'
  s=ins
  a=0
  c=0
  di=0
  a=a/256*256+ord(s[di+4])
  a-=0x2d
  if a!=0: 
    print '@@@'
    exit()
  si=di+4
  a=0
  while di!=si:
    a=a<<8
    a=a/256*256+ord(s[di])
    a-=0x30
    #print 'al:',a%256
    if a%256 >=4: 
    	print 'ERROR'
    	exit()
    di+=1
    #aad 4
    ah=a/256
    al=a%256
    a=ah*4+al
    c=c<<2
  c=a|c
  print i, ins, 'a:', bin(a)
  #print 'c:',bin(c)
  i+=1
