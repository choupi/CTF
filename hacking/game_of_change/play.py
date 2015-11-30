import random
from datetime import datetime
from time import sleep
import sys
import pexpect
import glibc_random as gr

def now_ts(tz=8):
    return int((datetime.now() - datetime(1970, 1, 1)).total_seconds())-3600*tz

def play(fn):
    sd=now_ts(8)
    print 'timestamp:', sd
    p=pexpect.spawn(fn)
    p.logfile = sys.stdout
    gr.mseed(sd)
    p.expect('credits] ->')
    p.sendline('1')
    for i in xrange(5):
        p.expect('Pick a number between 1 and 20:')
        sd=gr.mrand()
        #print sd, sd%20
        p.sendline('%d'%(sd%20+1))
        p.expect('Would you like to play again?')
        sleep(0.5)
        p.sendline('y')
    p.expect('Pick a number between 1 and 20:')
    sd=gr.mrand()
    #print sd, sd%20
    p.sendline('%d'%(sd%20+1))
    p.expect('Would you like to play again?')
    sleep(0.5)
    p.sendline('n')
    p.expect('credits] ->')
    sleep(5)
    exit(0)

if __name__ == '__main__':
    import sys
    play(sys.argv[1])
