def func(x=0,*args):
    print(args)

def fib(n):
    # return fib(n-1)+fib(n-2) if n>=2 else 1
    if n>=2:
        return fib(n-1)+fib(n-2)
    else:
        return 1
    print()
a=0
def love(age,firstname,*args,**kwargs):
    global a
    print('{}先生您好，今年您{}岁'.format(firstname,age))

# love(firstname=input('请问您贵姓：'),age=input('请问您贵庚：'))
'''
1.执行过程函数：函数体内完成一定的功能即可，没有返回值（返回值为None）
2.具有返回值的函数：函数体内完成一定的功能，并且返回一个结果到函数的调用处
3.
return 关键字返回值
'''
num=20
def jiechen(n):
    return jiechen(n-1)*n if n>=2 else 1
# print(jiechen(5))
"""

"""
def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
# print(fib(50))
def fib1(n):
    return fib(n-1)+fib(n-2) if n>=2 else 1
def func():
    globals()
'''
在内函数中如何使用上一层函数中的局部变量？
在内函数中如果想使用外层函数的变量，那么需要使用nonlocal函数
'''
def outer():
    '''
    
    :return:
    '''
    num=10
    def inner():
        #nonlocal关键字在局部函数中使用
        nonlocal  num
        num+=1
        print(num)
    inner()
outer()
# import pandas as pd
# df=pd.read_excel(r'C:\Users\Lenovo\Desktop\新建文件夹\账单.xlsx',sheet_name='22.03')
# print(df.head())
print(__doc__)
def hanshu():
    '''
    word
    :return:
    '''
    pass
print(__doc__)
'''
123456
'''
def multiple():
    '''
    当前函数的功能是打印九九乘法表
    :return:
    '''
    for i in range(1,10):
        print()
        for j in range(1,i+1):
            print('{}*{}={}'.format(j,i,i*j),end='  ')
def digui(num):
    print(num,end='')
    if num>0:
        digui(num-1)
    print(num)
print(jiechen(7))
print(7*6*5*4*3*2*1)
'''
解析当前函数的运行过程==>
'''