#-*- coding: UTF-8 -*-
'''
Created on 2016年6月24日

@author: sin
'''
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#指定需要解析的文档（这里使用的string代替），解析器，编码格式
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print ("get all links")
links = soup.find_all('a')
for link in links:
    print (link.name,link['href'],link.get_text())
    
print ("get lacie's url")
link_node = soup.find('a',href="http://example.com/lacie")
print (link_node.name,link_node['href'],link_node.get_text())
#支持正则表达式
print ("正则匹配")
link_node = soup.find('a',href=re.compile(r"ill"))#如果有r参数，有两个反斜线只需要写一个
print (link_node.name,link_node['href'],link_node.get_text())

print ("获取p段落文字")
p_node = soup.find('p',class_="title")#class需要加下滑线，因为class是html的关键字
print (p_node.name,p_node.get_text())
