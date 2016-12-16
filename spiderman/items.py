# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TutsplusItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()

class MarryItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    category = scrapy.Field()
    avatar = scrapy.Field()
    published_time = scrapy.Field()
    modified_time = scrapy.Field()