#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setting import mimidaili
from base_models import BaseCrawlModel

class CrawlMimi(BaseCrawlModel):
    def __init__(self,url):
        super(CrawlMimi,self).__init__(url)
        self.base_url = self.url + "/gngao/"
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


