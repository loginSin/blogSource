#coding=utf-8
'''
Created on 2016年6月26日

@author: sin
'''
import re,urllib2


url = "http://www.imooc.com/course/list"

buf = urllib2.urlopen(url)

urllist = re.findall(r"http://.+\.jpg",buf.read())

i=0

for u in urllist:
    print ("crawl image %d : %s"%(i+1,u))
    image_data = urllib2.urlopen(u)
    f = open(str(i)+".jpg",'w')
    f.write(image_data.read())
    i+=1