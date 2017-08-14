# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaogaozhongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    id = scrapy.Field()
    pid = scrapy.Field()
    sid = scrapy.Field()
    name = scrapy.Field()
    pass


class CityToSchoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    provinceId = scrapy.Field()
    cityId = scrapy.Field()
    townId = scrapy.Field()
    schoolId = scrapy.Field()
    pass

class SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
    schoolType = scrapy.Field()
    phone = scrapy.Field()
    top = scrapy.Field()
    pass

class ImageItem(scrapy.Item):
    id = scrapy.Field()
    type = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    pass