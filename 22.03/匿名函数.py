'''
匿名函数的意思就是说可以不使用def定义，并且这个函数也没有名字
'''
res=lambda x,y:x+y
print(res(4,4))
def func(sex):
    if sex=='男':
        return 'very man'
    else:
        return  'very beautiful'
res=lambda sex:"very man" if sex=='男' else "very beautiful"
print(res('1'))