# 引入 schedule 和 time
import schedule
import time

# 定义一个叫 job 的函数，函数的功能是打印 'I'm working...'
def job():
    print("Working in progress...")

# 部署情况
# 每 5s 执行一次 job() 函数
schedule.every(5).seconds.do(job)

# 检查部署的情况，如果任务准备就绪，就开始执行任务
while True:
    schedule.run_pending()
    time.sleep(1)