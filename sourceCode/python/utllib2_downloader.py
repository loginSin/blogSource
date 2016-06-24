#-*- coding: UTF-8 -*-
'''
Created on 2016年6月24日

@author: sin
'''
import urllib2,cookielib

url = "http://www.baidu.com"
print ("first")
response1 = urllib2.urlopen(url)
print ("status code %s" %response1.getcode())
print ("content length %s" %len(response1.read()))

print ("second")
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print ("status code %s" %response2.getcode())
print ("content length %s" %len(response2.read()))

print ("third")
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print ("status code %s" %response3.getcode())
print (cj)
print (response3.read())

