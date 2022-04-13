import scrapy
import bs4
from ..item


class DoubanSpider(scrapy.Spider):
    name = 'book_douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']

    for x in range(3):
        url = 'https://book.douban.com/top250?start={}'.format(x * 25)
        start_urls.append(url)

    # parse 是默认处理 response 的方法
    def parse(self, response):

        # 用 BeautifulSoup 解析 response
        bs = bs4.BeautifulSoup(response.text, 'html.parser')

        # 用 find_all 提取 <tr class="item"> 元素，这个元素里含有书籍信息
        datas = bs.find_all('tr', class_="item")

        # 遍历 data
        for data in datas:
            # 实例化 BookDoubanItem 这个类

            item = BookDoubanItem()

            # 提取出书名，并把这个数据放回 BookDoubanItem 类的 title 属性里

            item['title'] = data.find_all('a')[1]['title']

            # 提取出出版信息，并把这个数据放回 BookDoubanItem 类的 publish 里

            item['publish'] = data.find('p', class_='pl').text

            # 提取出评分，并把这个数据放回 BookDoubanItem 类的 score 属性里。

            item['score'] = data.find('span', class_='rating_nums').text

            # 打印书名

            print(item['title'])

            # yield item 是把获得的 item 传递给引擎
            yield item
