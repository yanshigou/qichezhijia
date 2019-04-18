# -*- coding: utf-8 -*-
import scrapy
from qichezhijia.items import SeriesItem


class SeriesSpider(scrapy.Spider):
    name = 'series'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['http://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]
    # start_urls = ['http://www.autohome.com.cn/grade/carhtml/A.html']

    def parse(self, response):
        for brandPart in response.xpath('body/dl'):
            brand_name = brandPart.xpath('dt/div/a/text()')[0].extract()
            seriesParts = brandPart.xpath('dd/ul/li')
            for seriesPart in seriesParts:
                try:
                    series = SeriesItem()
                    series['brand_name'] = brand_name
                    series['name'] = seriesPart.xpath('h4/a/text()')[0].extract()
                    series['url'] = seriesPart.xpath('h4/a/@href')[0].re(r'(//www\.autohome\.com\.cn/\d+)')
                    # print(series['name'])
                    # print(series)
                    yield series
                    # print(brand_name)
                    # print(seriesPart.xpath('h4/a/@href')[0].re(r'(//www\.autohome\.com\.cn/\d+)'))
                except:
                    pass