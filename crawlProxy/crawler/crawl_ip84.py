#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base_models import BaseCrawlModel
from bs4 import BeautifulSoup


class CrawlIp84Model(BaseCrawlModel):
    def __init__(self, url):
        super(CrawlIp84Model, self).__init__(url)
        self.para1 = 'gn'
        self.para2 = 'pn'
        self.para3 = 'gw'
        self.width = 100

    def gen_urls(self):
        url_list = []
        for i in xrange(self.width):
            url_list.append(self.url + "/" + self.para1 + "/" + str(i))
        return url_list

    def crawl_data(self, urls):
        for url in urls:
            content = self.s.get(url).content
            soup = BeautifulSoup(content)



