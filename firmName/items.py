# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirmnameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    name = scrapy.Field()
    addr = scrapy.Field()
    postcodes = scrapy.Field()
    industry = scrapy.Field()
    contacts = scrapy.Field()
    telNum = scrapy.Field()
    phoneNum = scrapy.Field()
    fax = scrapy.Field()
    website = scrapy.Field()
