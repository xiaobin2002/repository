# 导入所需的库和模块
from gevent import monkey
# 让程序变成异步模式
monkey.patch_all()
from gevent.queue import Queue
import gevent, requests, bs4, csv

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings()

# 创建队列对象，并赋值给 work
work = Queue()

# 前 3 个分类的前 3 页的食物记录的网址
url_1 = "https://food.hiyd.com/list-{type}-html?page={page}"
# 通过两个 for 循环，能设置分类的数字和页数的数字
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        # 然后，把构造好的网址用 put_nowait 方法添加进队列里
        work.put_nowait(real_url)

# 第 11 个分类的前 3 页的食物记录的网址
url_2 = "https://food.hiyd.com/list-132-html?page={page}"
# 通过 for 循环，能设置第 11 个常见食物分类的食物的页数
for x in range(1, 4):
    real_url = url_2.format(page=x)
    # 然后，把构造好的网址用 put_nowait 方法添加进队列里
    work.put_nowait(real_url)


# 定义 crawler 函数
def crawler(job):
    # 添加请求头

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # 当队列不是空的时候，就执行下面的程序
    while not job.empty():
        # 用 get_nowait() 方法从队列里把刚刚放入的网址提取出来
        url = job.get_nowait()
        # 用 requests.get 获取网页源代码
        res = requests.get(url, headers=headers, verify=False)
        # 用 BeautifulSoup 解析网页源代码
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        # 用 find 提取出 <b> 标签的内容,当前页面所属的分类
        category = bs_res.find('b').text
        # 用 find_all 提取出 <li> 标签的内容
        foods = bs_res.find_all('li')
        # 遍历 foods
        for food in foods:
            # 用 find_all在<li> 标签下，提取出第二个 <div> 标签中 <h3> 标签中的文本，也就是食物名称
            food_name = food.find('a').find_all('div')[1].find('h3').text
            # 用 find_all在<li >标签下，提取出第二个 <div> 标签中 <p> 标签中的文本，也就是食物热量
            food_calorie = food.find('a').find_all('div')[1].find('p').text
            # 打印食物的名称列表 result_list
            print([category, food_name, food_calorie])


# 创建空的任务列表
tasks_list = []
# 相当于创建了 5 个爬虫
for x in range(5):
    # 用 gevent.spawn() 函数创建执行 crawler() 函数的任务
    task = gevent.spawn(crawler(work))
    # 往任务列表添加任务
    tasks_list.append(task)
# 用 gevent.joinall 方法，启动协程，执行任务列表里的所有任务，让爬虫开始爬取网站
gevent.joinall(tasks_list)