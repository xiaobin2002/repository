from gevent import  monkey
monkey.patch_all()#把程序变成协作式运行
import  gevent#导入gevent模块
from gevent.queue import Queue
import requests,csv
from bs4 import  BeautifulSoup
url_list=[]
for i in range(3):
    url='https://book.douban.com/top250?start='+str(i*25)
    url_list.append(url)
headers = {"user-agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
               }
#创建队列对象，并赋值给work
work=Queue()
for url in url_list:
    work.put_nowait(url) #使用put_nowait方法可以把请求网址都放进队列里


def douban_top250_spider():
    # url_start = 'https://book.douban.com/top250'
    while not work.empty():#当队列不为空的时候就执行下面的程序
        start_url=work.get_nowait()#使用get_nowait函数

        res = requests.get(url, headers=headers)
        bs_data = BeautifulSoup(res.text, "html.parser")
        datas = bs_data.find_all('tr', class_='item')
        for book in datas:
            book_name = book.find('div', class_='pl2').find('a').text.replace("\n", "").replace(" ", "")
            name = '《' + book_name + '》'
            author = book.find('p', class_='pl').text.replace("\n", "").replace(" ", "")
            rating = book.find('span', class_='rating_nums').text
            with open("top250c", 'a', encoding='utf-8',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, author, rating])
#创建协程任务
task_list=[]#创建一个空的任务列表
for i in range(3):
    task=gevent.spawn(douban_top250_spider)
    task_list.append(task)
#使用gevent.joinall（）
gevent.joinall(task_list)

