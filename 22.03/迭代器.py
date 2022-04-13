'''
迭代器是python中最具特色的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住访问遍历的为之的对象
从集合的第一个元素开始访问，知道集合中的所有元素被访问完毕
迭代器只能从前往后一个一个的遍历，不能后退
迭代器是一个能被next（）函数，并不断反悔下一个只的对象成为迭代器（iterator迭代器对象）
'''
# for i in range(1,1000000000000):
#     print(i)
###可迭代对象
arr=['赵四','刘能','小沈阳','海参炒面']
r=iter(arr)
print(next(r))
print(next(r))
re=list(r)
print(re)
from collections.abc import Iterator ,Iterable
varstr='123456'
res=iter(varstr)
print(isinstance(varstr,Iterable))