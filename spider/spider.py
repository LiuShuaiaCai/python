#!/usr/bin/python

import requests
import re
from bs4 import BeautifulSoup

def download(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    for href in soup.findAll('a'):
        if re.match(r'http.*',href['href'],flags=0):
            print(href['href'])

if __name__ == '__main__':
    url = "http://toefl.kmf.com"
    download(url)
