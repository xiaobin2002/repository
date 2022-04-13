
from selenium import webdriver
import time
# 设置引擎为 Chrome，从本地打开一个 Chrome 浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html')

time.sleep(2)
# 使用 class_name 找到评论
comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
# 循环
for i in range(len(comments)):
    # 找到评论
    comment = comments[i].find_element_by_tag_name('p')
    # 打印评论
    print('评论' + str(i) + ':' + comment.text +'\n-------------------------------------------------')
# 关闭浏览器
driver.close()
