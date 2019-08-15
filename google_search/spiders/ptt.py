# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from google_search.items import PttSearchItem

class PttSpider(CrawlSpider):
    name = 'ptt'
    allowed_domains = ['google.com']
    start_urls = ['https://www.google.com/search?q="[問題]肚子痛"+site:www.ptt.cc']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.ptt.cc/.*'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/search\?q=.*'), follow=True),
    )

    def parse_item(self, response):
        item = PttSearchItem()
        item['title'] = response.xpath("/html[1]/body[1]/div[3]/div[1]/div[3]/span[2]/text()").get()
        item['content'] = response.xpath("normalize-space(/html[1]/body[1]/div[3]/div[1]/text())").get()

        yield item
