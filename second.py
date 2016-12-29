#!usr/bin/env python
# -*- utf-8 -*-

import urllib2
import re
base = "http://tj.focus.cn/search/3167_0_0_0_0_0_0_0_0_"
for i in range(2,4):
    response = urllib2.urlopen(base+'p'+str(i)+'.html')
    html = response.read()
    name = re.findall('lp-t-title[\s|\S]*?<span',html)
    addr = re.findall('<p>[\S|\s]*?\">',html)
    price = re.findall('f40\">[\d]*',html)
    tel = re.findall('400phone[\s|\S]{16}',html)
    
    f = open("./a.txt","a")
    for j in range(0,len(name)):
        f.write(name[j].split('>')[2].split('<')[0]+'\t\t')
        f.write(price[j].split('>')[1]+'\t\t')
#        f.write(price[j]+'\t\t')
        f.write(addr[j].split('\"')[1]+'\r\n')
    f.close()
    response.close()  

#urllib.urlretrieve(url, filename)
