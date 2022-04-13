import  json
def func(f):
    print(f,type(f))
# func('{1}')
# %matplotlib inline
# import  numpy as np
# from matplotlib import pyplot as plt
# x=np.linspace(-np.pi,np.pi,256)
# y=np.sin(x)
# plt.plot(x,y)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# # 在指定的间隔内返回均匀间隔的数字
# x = np.linspace(-np.pi,np.pi,256)
# # 正弦函数
# y = np.sin(x)
# #画图，使用不同的颜色和线条
# plt.plot(x,y,color='red',linewidth=1)
# # 获得当前图表的图像
# ax = plt.gca()
#
# # 设置图型的包围线
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_color('none')
# ax.spines['left'].set_color('none')
# 设置不显示坐标轴刻度
# plt.xticks([])
# plt.yticks([])

# plt.show()
'''
闭包函数

'''
money=0
def work():
    global money
    money+=100
def overtime():
    global money
    money+=200
def shopping():
    global money
    money-=50
work()
work()
overtime()
shopping()
def funcm():
    money=0
    def work():
        nonlocal  money
        money+=100
    def overtime():
        nonlocal  money
        money+=200
    def shopping():
        nonlocal  money
        money-=50
    return work
funcm()


