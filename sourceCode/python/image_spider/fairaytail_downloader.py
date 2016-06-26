#coding=utf-8
'''
Created on 2016年6月26日

@author: sin
'''
#在飞玩网下载妖精的尾巴全集漫画
import urllib2,os

url = "http://www.feiwan.net/zqmanhua/fairytail/manhua/"
#总集数
total_count =490
#根目录名称
name = "fairytail"

tmp = total_count
while tmp>=1:
    episode = tmp

    i = 0
    #漫画的总页数，可能会比真实的数据多一点
    count = 30
    #目录格式为fairytail/123/
    root_path = name+"/"+str(episode)+"/" 
    os.makedirs(root_path)
    while i < count:
        try:
            #拼接新的url
            new_url = url+str(episode)+"/"+str(i)+".png"
            print ("url : %s"%new_url)
            buf = urllib2.urlopen(new_url)
            data = buf.read()
            data_size = len(data)
            #检测是否大于50K
            if data_size > 50*1000:
                fout = open(root_path+str(i)+".png",'w')
                fout.write(data)
            i+=1
        except:
            print ("crawl image failed %d..."%i)
            
    tmp -= 1
