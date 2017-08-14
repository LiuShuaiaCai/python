# -*- coding: utf-8 -*-

import subprocess

# 查看list
# subprocess.check_call("scrapy list",shell=True)

# 运行爬虫
# subprocess.check_call("scrapy crawl hgz",shell=True)

# coding:utf-8

from scrapy import cmdline

cmdline.execute("scrapy crawl hgz".split())
