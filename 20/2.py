import  csv
f=open('1.py','w',newline='')
writer_csv=csv.writer(f)
a=[]
for i in range(50):
    a.append(i)
writer_csv.writerow(a)
# import csv
#
# # 需要写入的数据
# score1 = ['math', 95]
# score2 = ['english', 90]
#
# # 打开文件，追加 a, newline="" ，可以删掉行与行之间的空格
# file = open("score.csv", "a", newline="")
#
# # 设定写入模式
# csv_write = csv.writer(file)
#
# # 写入具体内容
# csv_write.writerow(score1)
# csv_write.writerow(score2)





