# -*- coding: utf-8 -*-
import re

import demjson
import scrapy
from circ.items import FileItem


class CfSpider(scrapy.Spider):
    name = 'tf'
    allowed_domains = ['threatfeeds.io']
    start_urls = ['https://threatfeeds.io/?tdsourcetag=s_pcqq_aiomsg']

    # parse函数有特殊功能，不能定义
    def parse(self, response):
        feeds = re.findall(r'var\sfeeds\s=(.*?);', response.body.decode(), re.S)[0]
        datas = demjson.decode(feeds)
        item = FileItem()
        urls = list()
        for data in datas:
            url = data.get("url")
            if url != "":
                urls.append(url)
        with open(r'C:\Users\20160712\Desktop\爬虫地址.txt', "r") as f:
            new_urls = f.readlines()
            for new_url in new_urls:
                urls.append(new_url)
        item["file_urls"] = urls
        yield item


