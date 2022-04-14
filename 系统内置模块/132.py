import pickle
import json
import numpy as np

a=3
print(id(a))
a=2
print(id(a))


# vars='hello world'
# res=pickle.dumps(vars)
# # res=pickle.loads(b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00\x8c\x0bhello world\x94.')
# print(res,'\n',type(res))
# vars={'name':'张三','age':20,'sex':'male'}
# res=pickle.dumps(vars)
with open('./data.txt','rb')as fp:
    res=pickle.load(fp)
# vardict=pickle.loads(res)
print(res)
