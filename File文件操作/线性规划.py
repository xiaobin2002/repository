a=10
b=8
c=7
# def doing_A():
#     global a,b
#     a-=2
#     b-=1
# def doing_B():
#     global a,b,c
#     a-=1
#     b-=1
#     c-=1
li=[]
for x in range(1,6):
    for y in range(1,8):
        if 2*x+y<=10 and x+y<=8 and y<=7:
            lirun=4*x+3*y
            li.append(lirun)
            print(lirun,'\t',x,y)
print(max(li))
            # print('总利润为{}k'.format(4*x+3*y),'甲机器{}件，乙机器{}件'.format(x,y))

