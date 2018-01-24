# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GreatschoolsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school_name = scrapy.Field()
    grades = scrapy.Field()
    street_address = scrapy.Field()
    csz = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    domain = scrapy.Field()
    
