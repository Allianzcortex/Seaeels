#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

from setting import xicidaili
from base_models import BaseCrawlModel


class CrawlXici(BaseCrawlModel):
    def __init__(self, url):
        super(CrawlXici, self).__init__(url)
        self.base_url = self.url + "/" + "nn" + "/"
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.xicidaili.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }

        self.cookies = {'CNZZDATA1256960793': '274300973-1471392046-%7C1472197',
                        '_free_proxy_session': 'BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTQ0YTgxZjUyZmJlYmZmYmM4NDAyMTdhMWExOWZlOTI4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXRZYlU1S0g5c0VINXZvYklyaHFYbEZQZ3luNkhaZlQwamhrWE40OHRmOFk9BjsARg%3D%3D--1d8b8de8baad92804991c6a0b97b8f150c53ee65'}
        self.proxies = {'http': "socks5://127.0.0.1:1080"}

        self.gen_urls()

    def gen_urls(self):
        self.url_list = [self.base_url + str(i) for i in xrange(100)]
        return self.url_list

    def crawl_data(self, url):
        content = self.s.get(headers=self.headers, proxies=self.proxies, url=url).content
        soup = BeautifulSoup(content, "lxml")
        for tr in soup.find_all('tr'):
            try:
                print tr.find_all('td')[1].string
            except IndexError:
                pass

        time.sleep(3)
