import scrapy
from ..items import DoubanMovieItem
from bs4 import  BeautifulSoup

class DoubanNewmovieSpider(scrapy.Spider):
    name = 'douban_newmovie' #这是scrapy爬虫程序的唯一标识
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        bs_res=BeautifulSoup(response.text,'html.parser')
        datas=bs_res.find_all('div',class_='pl2')
        for data in datas:
            item=DoubanMovieItem()
            item['name']=data.find('a').text.replace(' ','').replace('\n','')
            item['url']=data.find('a')['href']
            item['info']=data.find('p').text.replace(' ','').replace('\n','')
            item['rating']=data.find('span',class_='rating_nums').text
            yield item
