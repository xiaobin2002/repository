import time
h=0
def hanoi(n,a,b,c):
    global h
    if n>0:
        hanoi(n-1,a,c,b)
        h+=1
        hanoi(n-1,b,a,c)

# hanoi(30,'A','B','C')
def func(n):
    return 2*func(n-1)+1 if n>1 else 1
print(func(64))