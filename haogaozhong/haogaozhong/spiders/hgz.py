# -*- coding: utf-8 -*-

# 好高中

import scrapy
import urllib3
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from haogaozhong.items import HaogaozhongItem,CityToSchoolItem,SchoolItem,ImageItem

# class Haogaozhong(scrapy.Spider):
class Haogaozhong(CrawlSpider):
    name = "hgz"
    allowed_domains = ["haogaozhong.eol.cn"]
    start_urls = [
        "http://haogaozhong.eol.cn/school_area.php?province=",
    ]
    rules = (
        # Rule(LinkExtractor(allow=('school_area\.php\?province\=')), follow=True),
        Rule(LinkExtractor(allow=('school_area\.php\?province\=')), callback='province'),
    )

    startUrl = "http://haogaozhong.eol.cn/school_area.php?province="
    maxId = 0
    schoolId = 0
    citys = []

    # 默认方法parse
    # def parse(self, response):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, callback=self.province)


    # 获取省份名称province
    def province(self, response):
        for sel in response.xpath("//ul/li[@name='area']/a"):
            provinceVal = sel.xpath('./@value').extract_first()
            if provinceVal:
                provinceName = sel.xpath('./text()').extract_first()
                # id
                self .maxId += 1
                current = {"id":self.maxId, "pid":0, "name":provinceName.strip(), "sid":provinceVal}
                self.citys.append(current)

                # 实例化item
                item = HaogaozhongItem()
                item['type'] = 'city'
                item['id'] = self.maxId
                item['pid'] = 0
                item['sid'] = provinceVal
                item['name'] = provinceName.strip()
                yield item


                provinceUrl = self.startUrl+provinceVal
                request = scrapy.Request(provinceUrl, callback=self.city)
                request.meta['current'] = current
                yield request



    # 获取城市名称city
    def city(self, response):
        for sel in response.xpath("//ul/li[@name='city']/a"):
            cityNames = sel.xpath('./text()').extract()
            cityVals = sel.xpath('./@value').extract()
            items = response.meta['current']
            for cityVal,cityName in zip(cityVals,cityNames):
                pid = items['id']
                self.maxId += 1
                current = {"id":self.maxId,"pid":pid,"name":cityName.strip(),"sid":cityVal}
                self.citys.append(current)

                # 实例化item
                item = HaogaozhongItem()
                item['type'] = 'city'
                item['id'] = self.maxId
                item['pid'] = pid
                item['sid'] = cityVal
                item['name'] = cityName.strip()
                yield item

                cityUrl = response.url+"&city="+cityVal
                request = scrapy.Request(cityUrl, callback=self.town)
                request.meta['current'] = current
                yield request


    # 获取乡镇名称town
    def town(self, response):
        for sel in response.xpath("//div[@class='w_580 left red']/p[@id='town']"):
            townNames = sel.xpath('a/text()').extract()
            townVals = sel.xpath('a/@value').extract()
            items = response.meta['current']
            for townVal, townName in zip(townVals, townNames):
                pid = items['id']
                ppid = items['pid']
                self.maxId += 1
                current = {"id": self.maxId, "pid": pid, "ppid":ppid, "name": townName.strip(), "sid": townVal}
                self.citys.append(current)

                # 实例化item
                item = HaogaozhongItem()
                item['type'] = 'city'
                item['id'] = self.maxId
                item['pid'] = pid
                item['sid'] = townVal
                item['name'] = townName.strip()
                yield item


                townUrl = response.url + "&town=" + townVal
                request = scrapy.Request(townUrl, callback=self.school)
                request.meta['current'] = current
                yield request


    def school(self, response):
        current = response.meta['current']
        for schoolInfo in response.xpath('//div[contains(@class, "mar_t_30 overhidden")]'):
            self.schoolId += 1

            # 获取学校的信息
            schoolItem = SchoolItem()
            schoolItem['id'] = self.schoolId
            schoolItem['type'] = 'school'
            schoolItem['name'] = schoolInfo.xpath('./following-sibling::div[@class="p_bor"]/a/text()').extract_first()
            schoolItem['address'] = schoolInfo.xpath('./descendant::tr[1]/td[1]/text()').extract_first()
            schoolItem['url'] = schoolInfo.xpath('./descendant::tr[1]/td[2]/a/@href').extract_first()
            if schoolInfo.xpath('./descendant::tr[2]/td[1]/text()').extract_first().split('：')[1]:
                schoolItem['schoolType'] = schoolInfo.xpath('./descendant::tr[2]/td[1]/text()').extract_first().split('：')[1].strip()
            schoolItem['phone'] = schoolInfo.xpath('./descendant::tr[2]/td[2]/text()').extract_first().split('：')[1].strip()
            schoolItem['top'] = schoolInfo.xpath('./descendant::tr[3]/td[1]/text()').extract_first().split('：')[1].strip()
            yield schoolItem

            # 学校的图片
            imageItem = ImageItem()
            imageItem['id'] = self.schoolId
            imageItem['type'] = 'image'
            imageItem['image_urls'] = schoolInfo.xpath('./descendant::img/@src').extract()
            imageItem['image_paths'] = ''
            yield imageItem


            middleItem = CityToSchoolItem()
            middleItem['type'] = 'middle'
            middleItem['provinceId'] = current['ppid']
            middleItem['cityId'] = current['pid']
            middleItem['townId'] = current['id']
            middleItem['schoolId'] = self.schoolId
            yield middleItem

        # 爬取分页
        host = urllib3.get_host(response.url)
        nextPage = response.xpath("//div[@id='pagenav']/ul/li[3]/a/@href")
        if nextPage:
            nextUrl = host[0]+host[1]+nextPage
            request = scrapy.Request(nextUrl, callback=self.school)
            request.meta['current'] = current
            yield request
