# -*- coding:utf-8 -*-

from __future__ import absolute_import
from seaeels.sites.range_site import RangeSite
# from utils import write_to_output
from seaeels.models import BaseModels

# from app import Seaeels

if __name__ == '__main__':
    class DoubanModel(BaseModels):
        # name = StringField(pattern='.title.string')  # StringField 是需要进行说明的
        name = 'title'

    range_site = RangeSite(name='douban', model=DoubanModel)

    @range_site.route(start_url='https://book.douban.com/tag/互联网？start=',
                      page_range=xrange(0, 100, 20),
                      to_txtname='douban.txt')
    def crawl_douban():
        # write_to_output(db_name='douban.db')
        print 'done ---'


    crawl_douban()

    # seaeels = Seaeels()
    # seaeels.add_site(range_site)
    # seaeels.run()
