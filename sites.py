# -*- coding:utf-8 -*-
from functools import wraps

import requests
from bs4 import BeautifulSoup

a = 1


# class Site():
#     def __init__(self):
#         """
#
#         :return:
#         """
#
#     def crawl(self):
#         pass
#
#     def route():
#         def decorator(func):
#             # to-do something
#             return func
#
#         return decorator()


class RangeSite(object):
    def __init__(self, name, model):

        self.name = name
        self.item_list = {}
        for item in dir(model):
            if not item.startswith('__') and item is not 'save':
                self.item_list[item] = getattr(model, item)
        self.result_list = {}

    def __str__(self):
        return 'RangeSite {}'.format(self.name)

    def crawl(self, start_url=None, page_range=None):
        for index in page_range:
            url = start_url + str(index)

            soup = BeautifulSoup(requests.get(url).content, 'html.parser')
            for item, pattern in self.item_list.items():
                print item,pattern
                self.result_list[item] = soup.find_all(pattern)[0].string
                print soup.find_all(pattern)[0]
                print self.result_list[item]

    def route(self, start_url=None, page_range=None):
        def process_route(func):
            @wraps(func)
            def wrappers(**kwargs):  # 这里可以用 **kwargs 来更好地处理嘛
                self.crawl(start_url=start_url, page_range=page_range)
                return func()

            return wrappers

        return process_route
