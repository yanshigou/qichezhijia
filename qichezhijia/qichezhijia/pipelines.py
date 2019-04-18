# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi

from qichezhijia.items import BrandItem, SeriesItem, ModelItem


class QichezhijiaPipeline(object):
    def process_item(self, item, spider):
        return item


# 解析品牌入库
class MySqlPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            'MySQLdb',
            db='drive_collect',
            user='root',
            passwd='123456',
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8',
            use_unicode=False)

    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    # 写入数据库中
    @staticmethod
    def _conditional_insert(tb, item):
        # 品牌
        if isinstance(item, BrandItem):
            n = tb.execute('select * from car_brand where name = %s ', (item["name"],))
            if n == 1:
                tb.execute('update car_brand set pic = %s ,url = %s where name = %s',
                           (item["pic"], item["url"], item["name"]))
            else:
                tb.execute('insert into car_brand(name,pic,url) values(%s,%s,%s)',
                           (item["name"], item["pic"], item["url"]))
        # 车系
        elif isinstance(item, SeriesItem):
            n = tb.execute('select * from car_series where name = %s ', (item["name"],))
            if n == 1:
                tb.execute('update car_series set brand_name = %s ,url = %s where name = %s',
                           (item["brand_name"], item["url"], item["name"]))
            else:
                tb.execute('insert into car_series(name,brand_name,url) values(%s,%s,%s)',
                           (item["name"], item["brand_name"], item["url"]))

        else:
            pass

    # 错误处理方法
    @staticmethod
    def handle_error(failue):
        print('--------------database operation exception!!-----------------')
        print(failue)
