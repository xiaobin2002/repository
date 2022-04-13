from gevent import monkey

# monkey.patch_all() 能把程序变成协作式运行，就是可以帮助程序实现异步
monkey.patch_all()

# 导入 gevent、time、requests
import gevent, time, requests

# 记录程序开始时间
start = time.time()
# 把 8 个网站封装成列表
url_list = ['https://www.baidu.com/',
            'https://www.sina.com.cn/',
            'http://www.sohu.com/',
            'https://www.qq.com/',
            'https://www.163.com/',
            'http://www.iqiyi.com/',
            'https://www.tmall.com/',
            'http://www.ifeng.com/']


# 定义一个 crawler() 函数
def crawler(url):
    # 用 requests.get() 函数爬取网站
    r = requests.get(url, verify=False)
    # 打印网址、请求运行时间、状态码
    print(url, time.time() - start, r.status_code)


# 创建空的任务列表
tasks_list = []
# 遍历 url_list
for url in url_list:
    # 用 gevent.spawn() 函数创建任务
    task = gevent.spawn(crawler, url)
    # 往任务列表添加任务
    tasks_list.append(task)

# 执行任务列表里的所有任务，就是让爬虫开始爬取网站
gevent.joinall(tasks_list)
# 记录程序结束时间
end = time.time()
# 打印程序最终所需时间
print(end - start)