from gevent import  monkey
monkey.patch_all()
import requests
import csv
from bs4 import  BeautifulSoup

url_start='https://book.douban.com/top250'
headers={"user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
for i in range(2):
    page=i*25
    url='https://book.douban.com/top250?start='+str(page)
    res=requests.get(url,headers=headers)
    bs_data=BeautifulSoup(res.text,"html.parser")
    datas=bs_data.find_all('tr',class_='item')
    for book in datas:
        book_name=book.find('div',class_='pl2').find('a').text.replace("\n","").replace(" ","")
        name='《'+book_name+'》'
        author=book.find('p',class_='pl').text.replace("\n","").replace(" ","")
        rating=book.find('span',class_='rating_nums').text
        with open("douban_top250", 'a',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([name,author,rating])

