from PIL import Image
import numpy as np
import sys
import urllib2
import re

NPSS=str(np.array([255,255,255]))
def check_diff(img):
    #img = Image.open(sys.argv[1])
    #img.save('ttt.bmp')
    (w,h)=img.size
    print w, h
    arr = np.array(img)
    s=''
    for i in xrange(w):
        for j in xrange(h):
            ss=str(arr[i][j])
            if ss==NPSS: continue
            if len(s)==0: s=ss
            if s!=ss: 
                #print i, j, ss, s
                return (i, j, ss, s)
            #if sum(arr[i][j])!=216: print i, j, sum(arr[i][j])
            #print i, j, arr[i][j]

u='http://ctfquest.trendmicro.co.jp:43210/'
res=urllib2.urlopen(u+'click_on_the_different_color')
r=res.read()
print r
#rr=re.findall('window.location.href=\'([a-f0-9]+)\?', r)
rr=re.findall('[a-f0-9]{44}', r)[0]
print rr
while True:
    res=urllib2.urlopen(u+'img/'+rr+'.png')
    img=Image.open(res)
    (i, j, ss, s)=check_diff(img)
    print i, j, ss, s
    res=urllib2.urlopen(u+rr+'?x=%d&y=%d'%(j,i))
    r=res.read()
    print r
    rr=re.findall('[a-f0-9]{44}', r)[0]
    print rr
