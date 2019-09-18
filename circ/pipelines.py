# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import re
import uuid

from scrapy.pipelines.files import FilesPipeline


class CircPipeline(object):
    def process_item(self, item, spider):
        return item


class MyFilePipeline(FilesPipeline):
    # 此方法FilesPipeline和ImagesPipeline内部已经执行,可以省略不重写
    # def get_media_requests(self, item, info):
    #     for file_url in item['file_urls']:
    #         yield Request(file_url)

    # 此方法FilesPipeline和ImagesPipeline内部已经执行,可以省略不重写
    # def item_completed(self, results, item, info):
    #     file_paths = [x['path'] for ok, x in results if ok]
    #     if not file_paths:
    #         raise DropItem("Item contains no files")
    #     item['file_paths'] = file_paths
    #     return item

    # 如果要选择自己的文件名输出格式,必须重写FilesPipeline类的file_path方法
    def file_path(self, request, response=None, info=None):
        """
        自定义图片保存路径,以图片的url保存,重写前是图片的url经过MD5编码后存储
        """
        file_path = "".join(re.findall(r"[^/]+(?!.*/)", request.url))
        if file_path == '':
            file_path = uuid.uuid1()
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        return f'{date}/{file_path}'
