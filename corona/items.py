# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoronaItem(scrapy.Item):
   Date=scrapy.Field()
   Name=scrapy.Field()
   Active_cases=scrapy.Field()
   Cured=scrapy.Field()
   Deaths=scrapy.Field()
   Total=scrapy.Field()