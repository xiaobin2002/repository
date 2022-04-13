import scrapy
import bs4
from ..items import Class14Item


# 定义一个爬虫类Spider_GetJobInfo
class Spider_GetJobInfo(scrapy.Spider):
    # 定义爬虫的名字为GetJobs
    name = 'GetJobsInfo'
    # 定义允许爬虫爬取网址的域名——职友集网站的域名
    allowed_domains = ['www.jobui.com']
    # 定义起始网址——职友集企业排行榜的网址
    start_urls = ['https://www.jobui.com/rank/company/']

    # parse是默认处理response的方法
    def parse(self, response):
        # 用BeautifulSoup解析response（企业排行榜的网页源代码）
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # 用find_all提取<ul class_="textList flsty cfix">标签
        ul_list = bs.find_all('ul', class_="textList flsty cfix")
        # 遍历ul_list
        for ul in ul_list:
            # 用find_all提取出<ul class_="textList flsty cfix">元素里的所有<a>元素
            a_list = ul.find_all('a')
            # 再遍历a_list
            for a in a_list:
                # 提取出所有<a>元素的href属性的值，也就是公司id标识
                company_id = a['href']
                # 构造出包含公司名称和招聘信息的网址链接的list
                url = 'https://www.jobui.com{id}jobs'.format(id=company_id)
                # 用yield语句把构造好的request对象传递给引擎。用scrapy.Request构造request对象。callback参数设置调用parse_GetJobInfo方法。

                yield scrapy.Request(url, callback=self.parse_GetJobInfo)

    # 定义新的处理response的方法parse_GetJobInfo（方法的名字可以自己起）
    def parse_GetJobInfo(self, response):
        # 用BeautifulSoup解析response(公司招聘信息的网页源代码)
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # 用find方法提取出公司名称
        company = bs.find(class_="company-banner-name").text
        # 用find_all提取<div class_="job-simple-content">标签，里面含有招聘信息的数据
        datas = bs.find_all('div', class_="job-simple-content")
        # 遍历datas
        for data in datas:
            # 实例化Class14Item这个类
            item = Class14Item()
            # 把公司名称放回Class14Item类的company属性里
            item['company'] = company
            # 提取出职位名称，并把这个数据放回Class14Item类的position属性里
            item['position'] = data.find_all(
                'div', class_="job-segmetation")[0].find('h3').text
            # 提取出工作地点，并把这个数据放回Class14Item类的address属性里
            item['address'] = data.find_all(
                'div', class_="job-segmetation")[1].find_all('span')[0].text
            # 提取出招聘要求，并把这个数据放回Class14Item类的detail属性里
            item['detail'] = data.find_all(
                'div', class_="job-segmetation")[1].find_all('span')[1].text
            # 用yield语句把item传递给引擎
            yield item

