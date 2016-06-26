#coding=utf-8
'''
Created on 2016年6月26日

@author: sin
'''
import re,urllib2

url = "http://baozoumanhua.com/"

buf = urllib2.urlopen(url)

urllist = re.findall(r"http://.+",buf.read())

i=0

for u in urllist:
    try:
        if "png" in u:
            new_url = u[:u.find("png")+3]
            print ("crawl image %d:%s"%(i+1,new_url))
            f = open(str(i)+".png",'w')
            data = urllib2.urlopen(new_url)
            f.write(data.read())
            i += 1
    except:
        print ("crawl image failed:%s" %u)
