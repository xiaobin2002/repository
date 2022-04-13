tian=['甲','乙','丙','丁','午','己','庚','辛','壬','癸']
di=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥',]
index=0
col=0
num=0
# if __name__=='__main__':
#     while num<60:
#         col=num%10
#         index=num%12
#         print(tian[col]+di[index])
#         num+=1
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-np.pi,np.pi,1000)
y=np.sin(x)
plt.plot(x,y)
plt.show()