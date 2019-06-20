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
import json
from Config import *#
from Queue import Queue



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
        #把url放入队列
class Threadwrite(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue=queue
        self.lock=lock
        self.f=f#这里可能跟你的不太一样
        
        
        