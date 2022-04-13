# 从 selenium 库中调用 webdriver 模块
from selenium import webdriver
import time
# 设置引擎为 Chrome，从本地打开一个 Chrome 浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html')

time.sleep(2)
while True:
    try:
        clickformore = driver.find_elements_by_class_name('comment__show_all_link c_tx_thin c_bg_normal')
        time.sleep(1)
        clickformore.click()
    except:
        print("不能再点击加载更多啦")
        break
comments=driver.find_elements_by_class_name('comment__list')
# 循环
for i in range(len(comments)):
    # 找到评论
    comment = comments[i].find_elements_by_class_name('comment__text ')
    # 打印评论
    print('评论' + str(i+1) + ':' + comment[0].text +
          '\n-------------------------------------------------')
# 关闭浏览器
driver.close()
