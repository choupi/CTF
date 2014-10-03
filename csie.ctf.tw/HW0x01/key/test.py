import subprocess
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
  # 11011100011011100011001001001110
  ins='3130-1232-0302-'+ins+'\n'
  p=subprocess.Popen('./hw1_r3v', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  out=p.communicate(input=ins)
  print ins.strip(), out
  i+=1
