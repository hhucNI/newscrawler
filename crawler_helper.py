#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'nby'
import requests
import time
from requests.exceptions import RequestException
from multiprocessing import Pool
import multiprocessing as mp
from pyquery import PyQuery as pq
from Config import *
import json
import os
import re

def get_one_page(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
    try:
        res = requests.get(url,headers=headers)
        if res.status_code==200:
            print('爬取成功')
            return res.text
        return None
    except RequestException:
        return None


#json
def get_one_page_json(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
    try:
        res = requests.get(url,headers=headers)
        if res.status_code==200:
            #print('爬取成功')
            return res.json()
        return None
    except RequestException:
        return None
        
def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                origin_image = re.sub("list", "origin", image.get('url'))
                yield {
                    'image':  origin_image,
                    # 'iamge': image.get('url'),
                    'title': title
                }
    
       
def crawl_sohu_url(url):
    html=get_one_page(url)
    doc=pq(html)
    #print(doc)
    child_url_dict={}
    #类别：url的形式
    
    #a节点的text是类别，href是url
    
    li=doc('.news-nav.area li:first-child')
    li.remove()
    nodelist=doc('.news-nav.area li').items()
    print(nodelist)
    for node in nodelist:
        url=node.find('a').attr('href')
        type=node.find('a').text()
        
        child_url_dict[type]=url
    return child_url_dict
#print(crawl_sohu_url(SOHU_URL)) 
#测试


def crawl_news_url(mainurl):
    typedict={}
    dict=crawl_sohu_url(mainurl)#这里是搜狐官网
    for type,url in dict.items():
        #self.typedict.append(type)
        html=get_one_page(url)
            
        doc=pq(html)
        dict={}
        newsnodes=doc('.news-box').items()
            
        for newsnode in newsnodes:
            newstitle=newsnode.find('h4').text()
            newsurl=newsnode('a').attr('href')
                #newsurl='https'+newsurl
                #subhtml=ch.get_one_page(newsurl)
                #doc=pq(subhtml)
                #newspassage=doc('.article').text()
                
                 
            dict[newstitle]=newsurl
        typedict[type]=dict
    return typedict

    
    
def crawl_page_content(url):#改成仅仅处理一个url内容
    #这边可以拆开
    #把这个函数变成只处理一页的内容
    url='http:'+url
    doc=pq(get_one_page(url))
    content=doc('.article p').items()
    strlist=[]
    for p in content:
        if p.find('a'):
            p.find('a').remove()
        strlist.append(p.text())
    strlist2=strlist[1:-1]
    if len(strlist)>=4:
        str=strlist[0][4:]+'\n'+' '.join(strlist2)#要加标题的话在这一行加
    else:
        str='no'
    return str
    '''save_folder=os.path.join(os.path.curdir,'news')
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)'''
            
def clean_zh_text(text):
    # keep English, digital and Chinese
    comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]')
    return comp.sub('', text)
    #接下来对每个url进行访问，爬取
def save_data_to_txt(res,type,title):
    print('开始存储')
    save_folder=os.path.join(os.path.curdir,'news',type)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    title2=clean_zh_text(title)
    filename=save_folder+'/'+str(title2)+'.txt'
    if not filename in os.listdir(save_folder):
        with open(filename,'w',encoding='utf-8',errors='ignore') as f:
            f.write(res)
#print(get_one_page('//www.sohu.com/a/315006886_313745'))

# 子进程要执行的代码
'''def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')'''

'''def run(self):
        print('代理池开始运行')
#多进程代码片
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()
        
        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()
        
        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()'''