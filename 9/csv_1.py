import csv
f=open('2216.csv','r',newline='')
# list=[[1,2,3],
# #       [3,4,5],
# #       [6,7,8]
# # ]
# # csv_write=csv.writer(f)
# # csv_write.writerows(list)
# # f.close
res=csv.reader(f)
for i in res:
      print(i)