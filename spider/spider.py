#!/usr/bin/python

import requests
import re
from bs4 import BeautifulSoup

class Spider:
    # def __init__(self,url):
    #     self.url = url


    def download(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        for href in soup.findAll('a'):
            link = re.match(r'http(.*\/$)?.*',href['href'],flags=0)
            link2 = re.match(r'http(.*\/$)?.*',href['href'],flags=0)
            if link:
                link3 = link.group(0)
                print(link3)
                # Spider.download(self,link3)


    def crawl_sitemap(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        for href in soup.findAll('a'):
            if re.match(r'http.*', href['href'], flags=0):
                print(href['href'])

if __name__ == '__main__':
    url = "http://toefl.kmf.com"
    Spider().download(url)
