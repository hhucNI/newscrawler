#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'nby'
import crawler_helper as ch
import requests
import os
import time
from requests.exceptions import RequestException
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing as mp
from pyquery import PyQuery as pq
#print(crawler_helper.time.time())
from lxml import etree
import crawler_helper as ch#
import json
from Config import *#
from Queue import Queue
#from saver import Saver#
class Crawler(object):
    def __init__(self):
        #self.typedict={}
        #self.saver=Saver()
        self.mainurl=SOHU_URL
    def crawl_sohu(self):
        start=time.time()
        typedict=ch.crawl_news_url(self.mainurl)
        #print(typedict)
        for type,cont in typedict.items():
            #print(cont)
            if cont:
                
                for title,suburl in cont.items():
                    #print(suburl)
                    #print('******************')
                    #print(title)
                    res=ch.crawl_page_content(suburl)
                    #print(res)
                    ch.save_data_to_txt(res,type,title)#完成存储即可，不用管typedict结构\
        end=time.time()
        print(end-start)
        print('歇一会')
#crawler=Crawler()
#crawler.crawl_sohu() 
               
class Threadurl(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        pass

class Threadcrawl(threading.Thread):
    def __init__(self,url,queue,out_queue):
        threading.Thread.__init__(self):
        self.url=url
        self.queue=queue
        self.out_queue=out_queue
    def run(self):
        #从队列中拿url
        
             
        
            #标题：新闻url
            #类别：{标题：新闻url}

#html=ch.get_one_page('http://www.sohu.com/c/8/1460')
#print(html)