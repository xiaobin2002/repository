# 导入所需的库和模块
from gevent import monkey
# 让程序变成异步模式
monkey.patch_all()
from gevent.queue import Queue
import gevent, requests, bs4, csv



# 创建队列对象，并赋值给 work
work = Queue()

# 前 3 个常见食物分类的前 3 页的食物记录的网址
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
# 通过两个 for 循环，能设置分类的数字和页数的数字
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        # 然后，把构造好的网址用 put_nowait 方法添加进队列里
        work.put_nowait(real_url)

# 第 11 个常见食物分类的前 3 页的食物记录的网址
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
# 通过 for 循环，能设置第 11 个常见食物分类的食物的页数
for x in range(1, 4):
    real_url = url_2.format(page=x)
    # 然后把构造好的网址用 put_nowait 方法添加进队列里
    work.put_nowait(real_url)

# 请写出 crawler 函数和启动协程的代码：
def crawler():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # 当队列不是空的时候，就执行下面的程序
    while not work.empty():
        # 用 get_nowait() 方法从队列里把刚刚放入的网址提取出来
        url = work.get_nowait()
        # 用 requests.get 获取网页源代码
        res = requests.get(url, headers=headers, verify=False)
        # 用 BeautifulSoup 解析网页源代码
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        # 用 find_all 提取出 <li class="item clearfix"> 标签的内容
        foods = bs_res.find_all('li', class_='item clearfix')
        # 遍历 foods
        for food in foods:
            # 用 find_all 在 <li class="item clearfix"> 标签下，提取出第 2 个 <a> 元素 title 属性的值，也就是食物名称
            food_name = food.find_all('a')[1]['title']
            # 用 find_all 在 <li class="item clearfix"> 元素下，提取出第 2 个 <a> 元素 href 属性的值
            # 跟 'http://www.boohee.com' 组合在一起，就是食物详情页的链接。
            food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
            # 用 find 在 <li class="item clearfix"> 标签下，提取 <p> 元素，再用 text 方法留下纯文本，也提取出了食物的热量。
            food_calorie = food.find('p').text
            # 打印食物的名称。
            print(food_name)
task_list=[]
for i in range(4):
    task=gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
