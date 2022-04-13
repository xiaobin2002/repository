'''

'''
res=range(int(2.2),-1,-1)
res=iter(res)
# print(next(res))
# print(next(res))
"""
*iterables
"""
var1=[1,2,3,4]
var2=['1','2','3','4']
var3=(1,2,3,4)
#调用zip函数，祖晨新的元祖迭代器
#
# res=zip(var1,var2,var3)
# print(res,type(res))
# for i in res:
#     print(i)
x=[1,2,3,3.3,65,1489]
y=[4,5,6]

# print(*zip(x,y))
# import numpy as np
# π=np.pi
# print(π)
# print(hex(123))
def func(x):
    y=x**-1
    return y
res=sorted(x,reverse=True,key=lambda x:x**-1)
print(res)
res=map(lambda x:x**2,x)
print(next(res))
print(next(res))
print(next(res))
list1=['a','b','c','d']
res1=map(ascii,list1)
for i in res1:
    print(i)
from functools import reduce
def myfunc(n):
    if n%2==0:
        return True
    else:
        return False
res=filter(myfunc,x)
for i in res:
    print(i)

