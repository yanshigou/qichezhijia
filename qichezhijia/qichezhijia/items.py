# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QichezhijiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 品牌
class BrandItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pic = scrapy.Field()


# 车系
class SeriesItem(scrapy.Item):
    brand_name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()


# 车型
class ModelItem(scrapy.Item):
    series_name = scrapy.Field()
    name = scrapy.Field()
    group = scrapy.Field()
    price = scrapy.Field()
