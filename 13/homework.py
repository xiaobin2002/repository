from gevent import  monkey
monkey.patch_all()
import requests,gevent
from bs4 import  BeautifulSoup
from gevent.queue import Queue
work=Queue()
url_1='https://food.hiyd.com/list-{num1}-html?page={num2}'
for i in range(1,4):
    for j in range(1,4):
        real_url=url_1.format(num1=i,num2=j)
        work.put_nowait(real_url)

requests.packages.urllib3.disable_warnings()
def crawler():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url,headers=headers,verify=False)
        bs_res=BeautifulSoup(res.text,'html.parser')
        datas = bs_res.find_all('li')
        for data in datas:
            food_name=data.find('h3').text
            food_cal=data.find('p').text
            print(food_name,food_cal)


task_list=[]
for i in range(1,6):
    task=gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)