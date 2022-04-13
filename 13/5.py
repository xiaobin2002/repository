import requests
from bs4 import BeautifulSoup
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
url='https://food.hiyd.com/list-1-html?page=2'
res=requests.get(url,headers=headers,verify=False)
bs_res=BeautifulSoup(res.text,'html.parser')
datas=bs_res.find_all('li')
for data in datas:
    food_name=data.find('h3').text
    food_clo=data.find('p').text
    print(food_name,food_clo)
