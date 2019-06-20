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
from queue import Queue
import threading
# 覆写父类的run方法，
    # run方法以内为【要跑在子线程内的业务逻辑】
    #thread.start()会触发的业务逻辑

urls_queue = Queue()
data_queue = Queue()
#lock = threading.Lock()
'''class Threadurl(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
    #把typedict中的url放入队列
        typedict=ch.crawl_news_url(url)
        for type,cont in typedict.items():
            if cont:
                for title,suburl in cont.items():
                #
                    queue.put((title,suburl))'''
                    #为了爬取以及存储时写名字方便
def put_url_to_queue(typedict,queue):
    #将typedict中的url存入队列
    for type,cont in typedict.items():
        if cont:
            for title,suburl in cont.items():
                #
                queue.put((title,suburl,type))


#爬取内容
class Threadcrawl(threading.Thread):
    def __init__(self,in_queue,out_queue):
        threading.Thread.__init__(self)
        self.in_queue=in_queue
        self.out_queue=out_queue
        #url为搜狐网址
    def run(self):
        #从队列中拿url
        while True:
            urllist=self.in_queue.get()#原因参考line36
            content=ch.crawl_page_content(urllist[1])
            #title,suburl
            self.out_queue.put((urllist[0],content,urllist[2]))#title,res,type
            self.in_queue.task_done()
        
#写入
class Threadwrite(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        
        self.queue=queue
        #self.lock=lock
    def run(self):
        while True:
            contentlist=self.queue.get()
            cleaned_content=ch.clean_zh_text(contentlist[1])
            ch.save_data_to_txt(cleaned_content,contentlist[2],contentlist[0])#参数:内容，种类，标题
            self.queue.task_done()
            

#主函数
def main(url):
    start=time.time()
    typedict=ch.crawl_news_url(url)
    put_url_to_queue(typedict,urls_queue)
    #上面写的不好
    for i in range(4):
        t=Threadcrawl(urls_queue,data_queue)
        t.setDaemon(True)
        t.start()
    for i in range(4):
        t=Threadwrite(data_queue)
        t.setDaemon(True)
        t.start()
    urls_queue.join()
    data_queue.join()
    
    stop=time.time()
    print("耗时",stop-start)
    print('爬取完毕')
    
main(SOHU_URL)