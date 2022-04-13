from gevent import  monkey
monkey.patch_all()
import  gevent
from gevent.queue import  Queue
import  requests,csv
from bs4 import  BeautifulSoup
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
start_url='https://www.boohee.com/food'
work=Queue()
url_1='https://www.boohee.com/food/group/1'
url_2='https://www.boohee.com/food/group/2'
url_3='https://www.boohee.com/food/group/3'
#'https://www.boohee.com/food/group/5?page=2'
res=requests.get(url=start_url,headers=headers)
# print(res.status_code)
bs_data=BeautifulSoup(res.text,'html.parser')
# print(bs_data)
