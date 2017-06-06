#coding=utf-8

from scrapy import Spider
from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = [
        'http://dmoztools.net/Computers/Programming/Languages/Python/Books/'
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item = DmozItem()
            item['title'] = sel.xpath('a/div/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('div/text()').extract()
            yield item

        '''
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
            '''
