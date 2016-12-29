#!usr/bin/env python
# -*- utf-8 -*-

import urllib2
import re
base = "http://tj.focus.cn/search/3167_0_0_0_0_0_0_0_0_"

for i in range(1,8):
    response = urllib2.urlopen(base+'p'+str(i)+'.html?sale_status=1')
    if i==1:
        response = urllib2.urlopen(base+'0.html?sale_status=1')
    html = response.read()
    name = re.findall('lp-t-title[\s|\S]*?<span',html)
    addr = re.findall('<p>[\S|\s]*?\">',html)
    price = re.findall('lp-s-price[\s|\S]*?lp-s-zhe',html)
    tel = re.findall('400phone[\s|\S]{16}',html)
    
    f = open("./"+"selling"+".txt","a")
    f.write(str(i)+"page\r\n")
    pattern = re.compile(r'f40\">[\d]*')
    for j in range(0,len(name)):
        f.write(name[j].split('>')[2].split('<')[0]+'\t\t')
        if len(price)>j and price[j] is not None:
#            f.write(price[j]+'\t\t')
            p = pattern.search(price[j])
            if p:
                f.write(p.group().split('>')[1]+'\t\t')
        f.write(addr[j].split('\"')[1]+'\r\n')
    f.write("\r\n")
    f.close()
    response.close()  

#urllib.urlretrieve(url, filename)
