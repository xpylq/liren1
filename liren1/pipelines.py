# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class Liren1Pipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(item["image_url"], meta={"image_name": item["image_name"]})

    def file_path(self, request, response=None, info=None):
        return request.meta["image_name"] + ".jpg"
