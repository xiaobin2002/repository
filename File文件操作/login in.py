# how=int(input('欢迎光临，请选择您想要的功能：\n0注册\n1登录：\n'))
user_list=[]
pwd_list=[]
blacklist=[]
with open('./user.txt','a+')as fp:
    fp.seek(0)
    res=fp.readlines()
    for i in res:
        a=i.replace('\n','').replace('\t','')
        arr=a.split(':')
        user_list.append(arr[0])
        pwd_list.append(arr[1])

with open('./black.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)
    res=fp.readlines()
    for i in res:
        blacklist.append(i.strip())
def register():
    while True:
        user_name = input('欢迎注册，请输入用户名：')
        if user_name in user_list:
            print('当前用户名已存在，请更换')
        else:
            while True:
                password = input('请输入密码：')
                if len(password)>=3:

                    repassword = input('请确认密码：')
                    if password==repassword:
                        with open('./user.txt','a+',encoding='utf-8')as fp:
                            fp.write('{}:{}\n'.format(user_name,password))
                        print('恭喜你，注册成功')
                        break
                    else:
                        print('两次密码不一致，请重新输入')
                else:
                    print('密码格式不正确')
            break

def login():
    errornum = 3
    while True:
        username=input('请输入用户名：')
        if username in user_list:
            if username in blacklist:
                print('当前用户处于锁定状态，无法登陆')
            else:
                while True:
                    pwd=input('请输入密码')
                    inx=user_list.index(username)
                    if pwd_list[inx]==pwd:
                        print('登录成功')
                        break
                    else:
                        errornum-=1
                        # print('密码错误，请重新输入')
                        if errornum==0:
                            print('您已连续三次输错密码，您的账户即将被锁定')
                            with open('./black.txt','a+',encoding='utf-8') as fp:
                                fp.write(username+'\n')
                            break
                        else:
                            print('您还剩{}次机会'.format(errornum))


                break


        else:
            print('用户名不存在，请重新输入')

# method=int(input('欢迎光临本网站，请输入您需要的服务：(1.注册 2.登录)'))
if __name__=='__main__':
    while True:
        st='''
        *****************************
        ***注册(1) 登录(2) 退出(任意键)**
        ***************************** 
        '''
        print(st)
        method=int(input('请输入相应的数字'))
        if method==1:
            register()
        elif method==2:
            login()
        else:
            print('欢迎下次体验')
            break
