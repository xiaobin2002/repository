# fp=open('./1.text','r',encoding='utf-8')
# res=fp.read()
# fp.close()
# print(res)
with open('./1.txt','a+',encoding='utf-8')as fp:


    fp.seek(0,2)
    res=fp.read()

    print(res)



    # fp.seek(0)#设置当前指针的位置seek（0）最开始的位置
    # res = fp.read()
    # print(res)