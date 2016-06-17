#/usr/bin/env python3.5
# -*- coding: utf-8 -*-
__author__ = 'zenway33'

from bs4 import BeautifulSoup
import requests
import time
import random
import re
import os

headers = {
       #'User-Agent': ua,
       'User-Agent': 'Mozilla/5.8 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding' : 'gzip, deflate, sdch',
       #'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
       'Connection': 'keep-alive'
}


web_url = 'http://www.dytt8.net/'
wb_data = requests.get(web_url,headers=headers)
wb_data.encoding = 'gb2312'
soup = BeautifulSoup(wb_data.text, 'lxml')
#print(soup.prettify())
#header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.title_all > p > strong
titles = soup.select('div.title_all > p > strong')
#header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.co_content8 > ul > table > tbody > tr:nth-child(4) > td:nth-child(1) > a:nth-child(2)
#<a href="/html/gndy/dyzz/20160610/51200.html">2016年传记喜剧《飞鹰艾迪》BD中英双字幕</a>
links = [a.attrs.get('href') for a in soup.select('a[href^=/html/gndy/dyzz/2016]')]
#header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.co_content8 > ul > table > tbody > tr:nth-child(4) > td:nth-child(1) > a:nth-child(2)
#header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.title_all
#moive_names = soup.select('tr > td > a')
#header > div > div.bd2 > div.bd3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div.co_content8 > ul > table > tbody
moive_names = soup.select('div.co_content8')
print(moive_names)
#print(titles)
print(links)


for moive_name in moive_names:
    moive_name = moive_name.get_text()
    print(moive_name)


'''
for moive_name,link  in zip(moive_names,links):
    data = {
        'moive_name' : moive_name.get_text(),
        'link' : link
    }
    print(data)
'''

#print(links)
'''
for text in hot_moives:
    print(text.decode('utf-8').encode('gbk'))
'''
