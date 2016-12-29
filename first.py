import requests
import urllib
import re
import random
from time import sleep
def main():
url='http://tj.focus.cn/search/3167_0_0_0_0_0_0_0_0.html'
headers={}
i=1
for x in xrange(20,3600,20):
content=requests.post(url,headers=headers,timeout=10).text
#用post提交form data
results=re.findall('<div class=\"clear1\">*s-lp-ul',content) 
#在爬下来的json上用正则提取图片地址，去掉_m为大图 
for result in results:
try:
name=result.replace('\\','')
#去掉\字符这个干扰成分
pic=img+'.jpg'
path='e:\\bs4\\result.txt'
#声明存储地址及图片名称
urllib.urlretrieve(pic,path)
#下载图片
print u'下载了第'+str(i)+u'张图片'
i+=1
sleep(random.uniform(0.5,1))
#睡眠函数用于防止爬取过快被封IP
except:
print u'抓漏1张'
pass
sleep(random.uniform(0.5,1))

if __name__=='__main__':

main()
