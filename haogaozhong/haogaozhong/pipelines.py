# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import json

class HaogaozhongPipeline(object):

    def open_spider(self, spider):
        self.city = open('city.json', 'w+')
        self.middle = open('middle.json', 'w+')
        self.school = open('school.json', 'w+')

    def close_spider(self, spider):
        self.city.close()
        self.middle.close()
        self.school.close()

    def process_item(self, item, spider):
        print(item)
        line = json.dumps(dict(item)) + "\n"
        # 写入 JSON 数据
        if item['type'] == 'city':
            self.city.write(line)
        elif item['type'] == 'middle':
            self.middle.write(line)
        elif item['type'] == 'school':
            self.school.write(line)
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['type']=='image':
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        if item['type']=='image':
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                raise DropItem("Item contains no images")
            item['image_paths'] = image_paths[0]
            item['image_urls'] = item['image_urls'][0]
            return item