# -*- coding:utf-8 -*-

import requests


def judge_ip(ip):
    url = "baidu.com"
    proxies = {"http": "http://{}".format(ip)}
    try:
        r = requests.get(url,proxies=proxies)
        return True
    except requests.exceptions.HTTPError:
        return False

#
# def write_to_output(**kwargs):
#     if 'models' not in kwargs.keys():
#         raise ValueError("You must clarify at least one model")
#
#     if 'db_name' in kwargs.keys():
#         pass
#     elif 'txt_name' in kwargs.keys():
#         with open(txt_name+'.txt','w+'):
#             for
