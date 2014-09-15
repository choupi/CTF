import Image
import sys

img = Image.open(sys.argv[1])
pixels = img.load()
px=[]
pw=256
for i in xrange(pw):
	for j in xrange(pw):
		#for x in pixels[j,i]: px.append(x)
		px.append(pixels[j,i][2])
out=[]
ss=''
c=0
for i in xrange(len(px)):
	#if px[i]&0x2: ss+='1'
	#else: ss+='0'
	if px[i]&0x1: ss='1'+ss
	else: ss='0'+ss
	c=(c+1)%8
	if c==0:
		out.append(int(ss,2))
		#print ss
		ss=''
print len(out)
print ''.join(map(chr,out))

