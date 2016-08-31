#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
# requests=requests.session()

import redis
from multiprocessing.dummy import Pool as ThreadPool


# from ..setting import host,port


class BaseCrawlModel(object):
    def __init__(self, url):
        self.url = url
        self.s = requests
        # self.r=redis.StrictRedis(host=host,port=port,db=0)

    def gen_urls(self):
        pass

    def crawl_data(self, url):
        pass

    def write_to_redis(self, country, ip):
        # self.r.zadd(key,ip)
        pass

    def start(self):
        pool = ThreadPool(processes=4)
        pool.map(self.crawl_data, self.url_list)
        pool.close()
        pool.join()
