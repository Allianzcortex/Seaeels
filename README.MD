one minimum available application are as below:

```
class DoubanModel(BaseModels):
        # name = StringField(pattern='.title.string')  # StringField id required to be declare
        name = 'title'

    range_site = RangeSite(name='douban', model=DoubanModel)

    @range_site.route(start_url='https://book.douban.com/tag/互联网？start=',
                      page_range=xrange(0, 100, 20))
    def crawl_douban():
        # write_to_output(db_name='douban.db')
        print 'done ---'
```
