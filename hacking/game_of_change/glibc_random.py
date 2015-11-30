
_rand_table=[]

def LCG(s):
    a=1103515245
    c=12345
    m=2147483648
    #s=(a*s+c)%m
    s=(a*s+c)&0x7fffffff
    return s

def int32(x):
    x=x&0xffffffff
    if x>0x7fffffff:
        x=0x100000000-x
        if x<2147483648: return -1*x
        else: return -2147483648
    return x

def mseed(s):
    _rand_table.append(s)
    for i in xrange(30):
      _rand_table.append((16807 * _rand_table[-1]) % 2147483647)
      if (_rand_table[i] < 0):
        _rand_table[i] += 2147483647
    for i in xrange(31, 34):
      _rand_table.append(_rand_table[i-31])
    for i in xrange(34, 344):
      _rand_table.append(int32(_rand_table[i-31] + _rand_table[i-3]))

def mrand():
    _rand_table.append(int32(_rand_table[-31]+_rand_table[-3]))
    if _rand_table[-1]<0: return (_rand_table[-1]+0x100000000)>>1
    return _rand_table[-1]>>1

if __name__ == '__main__':
    import sys
    if len(sys.argv)>1: mseed(int(sys.argv[1]))
    else: mseed(1)
    for i in xrange(10): print mrand()
