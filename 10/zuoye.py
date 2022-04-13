from selenium import  webdriver
import  time
#https://xiaoke.kaikeba.com/example/wordpress/网址
driver=webdriver.Chrome()
driver.get('https://xiaoke.kaikeba.com/example/wordpress/')
tiaozhuan=driver.find_element_by_link_text('开课吧无敌好吃的食堂一周菜谱')
time.sleep(1)
tiaozhuan.click()
login_1=driver.find_element_by_link_text('登录')
time.sleep(1)
login_1.click()
time.sleep(2)
login=driver.find_element_by_id('user_login')
login.send_keys('kaikeba')
mima=driver.find_element_by_id('user_pass')
mima.send_keys('kaikeba888')
denglu=driver.find_element_by_id('wp-submit')
denglu.click()
comment=driver.find_element_by_id('comment')
comment.send_keys('selenium大法好！aaaaaaaaa')
fabiao=driver.find_element_by_id('submit')
fabiao.click()


