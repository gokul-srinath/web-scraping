# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebTrafficItem(scrapy.Item):
    Domain=scrapy.Field()
    Pagespeed=scrapy.Field()
    Yslow=scrapy.Field()
    Onload=scrapy.Field()
    Full_load=scrapy.Field()
    Requests=scrapy.Field()
    Total_size=scrapy.Field()
