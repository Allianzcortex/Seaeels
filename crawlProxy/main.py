#!/usr/bin/env python
# -*- coding:utf-8 -*-

from crawler.crawl_xici import CrawlXici
from crawler.setting import xicidaili


if __name__=='__main__':

    crawlXici=CrawlXici(xicidaili)
    crawlXici.start()