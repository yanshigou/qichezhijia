# -*- coding: utf-8 -*-
import scrapy
from qichezhijia.items import BrandItem


class BrandSpider(scrapy.Spider):
    """
    ['http://www.autohome.com.cn/grade/carhtml/A.html', 'http://www.autohome.com.cn/grade/carhtml/B.html',
    'http://www.autohome.com.cn/grade/carhtml/C.html', 'http://www.autohome.com.cn/grade/carhtml/D.html',
    'http://www.autohome.com.cn/grade/carhtml/E.html', 'http://www.autohome.com.cn/grade/carhtml/F.html',
    'http://www.autohome.com.cn/grade/carhtml/G.html', 'http://www.autohome.com.cn/grade/carhtml/H.html',
    'http://www.autohome.com.cn/grade/carhtml/I.html', 'http://www.autohome.com.cn/grade/carhtml/J.html',
    'http://www.autohome.com.cn/grade/carhtml/K.html', 'http://www.autohome.com.cn/grade/carhtml/L.html',
    'http://www.autohome.com.cn/grade/carhtml/M.html', 'http://www.autohome.com.cn/grade/carhtml/N.html',
    'http://www.autohome.com.cn/grade/carhtml/O.html', 'http://www.autohome.com.cn/grade/carhtml/P.html',
    'http://www.autohome.com.cn/grade/carhtml/Q.html', 'http://www.autohome.com.cn/grade/carhtml/R.html',
    'http://www.autohome.com.cn/grade/carhtml/S.html', 'http://www.autohome.com.cn/grade/carhtml/T.html',
    'http://www.autohome.com.cn/grade/carhtml/U.html', 'http://www.autohome.com.cn/grade/carhtml/V.html',
    'http://www.autohome.com.cn/grade/carhtml/W.html', 'http://www.autohome.com.cn/grade/carhtml/X.html',
    'http://www.autohome.com.cn/grade/carhtml/Y.html', 'http://www.autohome.com.cn/grade/carhtml/Z.html']

    """
    name = 'brand'
    allowed_domains = ['autohome.com.cn']
    # start_urls = ['https://www.autohome.com.cn/car/']
    start_urls = ['http://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]
    # start_urls = ['http://www.autohome.com.cn/grade/carhtml/A.html']

    def parse(self, response):
        # print(response.xpath('//*[@id="tab-content-item2"]').xpath('//*[@id="boxA"]').xpath('//*[@id="33"]/dd/div[1]/a/text()')[0].extract())
        # yiqi_dazongaodi = response.xpath('//*[@id="tab-content-item2"]').xpath('//*[@id="boxA"]').xpath('//*[@id="33"]/dd/div[1]/a/text()')[0].extract()
        for brandPart in response.xpath('body/dl'):
            brand = BrandItem()
            brand['url'] = brandPart.xpath('dt/a/@href')[0].extract()
            brand['name'] = brandPart.xpath('dt/div/a/text()')[0].extract()
            brand['pic'] = brandPart.xpath('dt/a/img/@src')[0].extract()
            yield brand
            print(brand['name'])
