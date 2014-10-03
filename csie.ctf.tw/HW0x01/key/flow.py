s='0123-1230-1110-0011-'
a=0
c=0
for i in xrange(0,len(s),5):
  di=i
  a=0
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
  print 'a:', bin(a)
  print 'c:',bin(c)
st=a
a=c
c+=1
d=0x4ec4ec4f
#mul edx
d*=a
print "d:", hex(d)
a=d&0xffffffff
d=d>>32
d=d>>2
print "d:", hex(d)
#hex((0x10f4c8cb<<34)/0x4ec4ec4f)=0xdc6e324e
# c should be 0xdc6e324e (11011100011011100011001001001110)
if d!=0x10f4c8cb: 
  print "WWW"
  st=0
#lea    (%edx,%edx,2),%eax
#lea    (%edx,%eax,4),%eax
c-=a
d=0x1a330fff
# c should be 13
if c>0: d=d>>c
print "d:", hex(d)
if d!=0xd198: 
  print "QQQ"
  st=0
#test   %eax,%eax


