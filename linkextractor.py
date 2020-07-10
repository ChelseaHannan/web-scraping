# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ElementSpiderSpider(CrawlSpider):
    name = '#spider'
    allowed_domains = ['#domain']
    start_urls = ['#start urls']

    rules = (
        Rule(LinkExtractor(''), callback='parse_item', follow=True),
    )

    # grabs all specified elements from a website, using h1 as example
    def parse_item(self, response):
        h1 = response.xpath('//h1/text()').getall()
        for i in h1:
            yield {
                'h1 text': i
            }

