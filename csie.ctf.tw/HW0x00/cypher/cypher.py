import hashlib
import re
import pexpect
import sys
import string
import base64
import zlib

def c2(s):
	ccc2=string.maketrans(
		'hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefg',
		'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	return string.translate(s, ccc2)

def c3(s):
	ss='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	r=''
	for x in xrange(0,len(s)):
		i=ss.find(s[x])
		r+=ss[(i-x-1)%len(ss)]
	return r

def c4(s):
	ccc4=string.maketrans(
		'rlN7utjd0S5qp1EX2nT34eWQhoVHJigwGMmFYzxcvPDkK8CayR6LBZfAsbU9IO',
		'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	return string.translate(s, ccc4)

def c5(s):
	ss='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	key='APPLE'
	r=''
	for x in xrange(0,len(s)):
		i=ss.find(s[x])
		off=ss.find(key[x%len(key)])
		r+=ss[(i-off)%len(ss)]
	return r

def c6(s):
	ss='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	r=''+s[0]
	c=ss.find(s[0])
	for x in xrange(1,len(s)):
		i=ss.find(s[x])
		rr=ss[(i-c)%len(ss)]
		c=ss.find(s[x])
		r+=rr
	return r

def c7(s):
	ss=base64.b64decode(s)
	return ss.strip()

def c8(s):
	ss=''
	for i in xrange(0,len(s),2): ss+=chr(int(s[i:i+2], 16))
	return zlib.decompress(ss, zlib.MAX_WBITS|16)

def c9(s):
	ss='kqmpsotjlunigeabfrcdh'
	tt='abcdefghijklmnopqrstu'
	r=''
	for i in xrange(0, len(tt)):
		r+=s[ss.index(tt[i])]
	return r

p = pexpect.spawn('nc ctf.tw 6002')
#p.setecho(True)
p.logfile = sys.stdout

for i in xrange(1,11):
	p.expect('Ciphertext: ')
	x=p.readline()
	p.expect('Plaintext:')
	if i==1:
		p.sendline(x.strip().strip())
	if i==2:
		#p.sendline(string.ascii_letters)
		#print c2(x)
		p.sendline(c2(x.strip()).strip())
	if i==3:
		p.sendline(c3(x.strip()).strip())
	if i==4:
		p.sendline(c4(x.strip()).strip())
	if i==5:
		#p.sendline('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		p.sendline(c5(x.strip()).strip())
	if i==6:
		#p.sendline('1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') # 11247bgmtBKU5huIXduM5pK6tRgG7z2w1x4CbLmYBfUAhZIsdZMApf6YRLGCzxw
		#p.sendline('abbbbbbbbbbbbbbb') #abcdefghijklmnop
		#p.sendline('acccccccccccccc') #acegikmoqsuwyAC
		#p.sendline('abcdefghijkl') #abdgkpvCKT3e
		p.sendline(c6(x.strip()).strip())
	if i==7:
		#print [hex(ord(zzz)) for zzz in c7(x)]
		p.sendline(c7(x.strip()).strip())
	if i==8:
		p.sendline(c8(x.strip()))
#		p.sendline('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
	if i==9:
		p.sendline(c9(x.strip()))
		#p.sendline('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		#p.sendline('abcdefghijklmnopqrstu')
		#p.sendline('bcaaaaaaaaaaaaaaaaaaa')
