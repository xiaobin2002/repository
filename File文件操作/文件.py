# fp=open(r'C:\Users\Lenovo\Desktop\新建文件夹\账单.xlsx','r')
# print(fp.read())
import  numpy
for i in range(1,100):
    for j in range(1,100):
        if i+j==i*i+j*j:
            print(i,j)
def fib(n):
    return fib(n-1)+fib(n-2) if n>2 else 1
print(fib(40))