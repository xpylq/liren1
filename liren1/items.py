# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Liren1Item(scrapy.Item):
    # define the fields for your item here like:
    image_url = scrapy.Field()
    pass


class ImageItem(scrapy.Item):
    image_url = scrapy.Field()
    image_name = scrapy.Field()
    images = scrapy.Field()
