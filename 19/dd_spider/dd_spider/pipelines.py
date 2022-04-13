# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import  openpyxl
class DdSpiderPipeline:
    def __init__(self):
        # 创建工作薄
        self.wb = openpyxl.Workbook()
        # 定位活动表
        self.ws = self.wb.active
        # 用append函数往表格添加表头
        self.ws.append(['书名', '作者', '价格'])

    # process_item是默认的处理item的方法，就像parse是默认处理response的方法
    def process_item(self, item, spider):
        # 把公司名称、职位名称、工作地点和招聘要求都写成列表的形式，赋值给line
        line = [
            item['name'], item['author'], item['price']
        ]
        # 用append函数把公司名称、职位名称、工作地点和招聘要求的数据都添加进表格
        self.ws.append(line)
        # 将item丢回给引擎，如果后面还有这个item需要经过的itempipeline，引擎会自己调度
        return item

    # close_spider是当爬虫结束运行时，这个方法就会执行
    def close_spider(self, spider):
        # 保存文件
        self.wb.save('rank.xlsx')
        # 关闭文件
        self.wb.close()
