# 导入所需的库和模块
from gevent import monkey
# 让程序变成异步模式
monkey.patch_all()
from gevent.queue import Queue
import gevent, requests, bs4, csv

# 创建队列对象，并赋值给work。
work=Queue()
# 前 3 个常见食物分类的前 3 页的食物记录的网址
url_1='http://www.boohee.com/food/group/{type}?page={page}'
for i in range(1,4):
    for j in range(1,4):
        real_url = url_1.format(type=i, page=j)
        work.put_nowait(real_url)
# 第 11 个常见食物分类的前 3 页的食物记录的网址
url_2='https://www.boohee.com/food/view_menu?page={page}'
for i in range(1,4):
    real_url=url_2.format(page=i)
    work.put_nowait(real_url)
    # print(url_2)

# 打印队列
print(work)