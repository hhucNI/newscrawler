
import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re
import json

class Saver(object):
    '''def __init__(self):
        pass'''
    def save_data_to_txt(data,type,title):
        print('开始存储')
        save_folder=os.path.join(os.path.curdir,'news',type)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        filename=str(title)+'.txt'
        with open(filename,'w') as f:
            f.write(data)
            
            
        
        



    