import  openpyxl
# 打开的指定的工作簿
wb = openpyxl.load_workbook('1415.xlsx')
# 指定读取的工作表的名称
sheet = wb['开课吧']
# 获取
A1_value = sheet['b4'].value
print(A1_value)