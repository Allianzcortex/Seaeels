# -*- coding:utf-8 -*-
"""
utils.py include some useful utils that will be used
judge_ip will judge whether ip crawled can be use
write_to_db will write content to database(SQLite)
write_to_txt will write content to txt file
"""
import os

abs_path = os.path.abspath(__name__)
# os.chdir('../..')

import requests


def judge_ip(ip):
    url = "baidu.com"
    proxies = {"http": "http://{}".format(ip)}
    try:
        r = requests.get(url, proxies=proxies)
        return True
    except requests.exceptions.HTTPError:
        return False


def write_to_db(db_name, content):
    pass


def write_to_txt(txt_name, content):
    # if os.path.isfile(txt_name):
    #     raise ValueError("The {} has already existed".format(txt_name))
    print content
    with open(txt_name, 'w') as inp:
        inp.write(content.keys()[0])
