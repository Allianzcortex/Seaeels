# -*- coding:utf-8 -*-
"""
The RangeSite is to deal the website which owns the sequential url
like "https://book.douban.com/tag/互联网？start="
filename is split by underscore to improve readability
"""
from functools import wraps
import requests
from bs4 import BeautifulSoup

from .base_site import BaseSite
# from Seaeels import NotIdentifiedError
#from seaeels.errors import NotIdentifiedError
from seaeels.errors import NotIdentifiedError
from seaeels.utils import write_to_db
from seaeels.utils import write_to_txt


class RangeSite(BaseSite):
    def crawl(self, start_url=None, page_range=None):
        for index in page_range:
            url = start_url + str(index)
            soup = BeautifulSoup(requests.get(url).content, 'html.parser')
            for item, pattern in self.item_list.items():
                print item, pattern
                self.result_list[item] = soup.find_all(pattern)[0].string
                print soup.find_all(pattern)[0]
                print self.result_list[item]

    def write_db(self, db_name):
        write_to_db(db_name, self.result_list)

    def write_txt(self, txt_name):
        write_to_txt(txt_name, self.result_list)

    def route(self, start_url=None, page_range=None,**kwargs):
        print kwargs
        path_to=kwargs
        def process_route(func,path_to=path_to):
            @wraps(func)
            def wrappers(*args,**kwargs):  # 这里可以用 **kwargs 来更好地处理嘛
                print kwargs
                self.crawl(start_url=start_url, page_range=page_range)
                if 'to_dbname' in path_to:
                    self.write_db(path_to.get('to_dbname'))
                elif 'to_txtname' in path_to:
                    self.write_txt(path_to.get('to_txtname'))
                else:
                    raise NotIdentifiedError('db_name or txt_name')
                return func(*args,**kwargs)

            return wrappers
        return process_route

    def __str__(self):
        return "RangeSite {}".format(self.name)