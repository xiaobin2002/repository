# 引用 openpyxl
import openpyxl
# 利用 openpyxl.Workbook() 函数创建新的 workbook（工作薄）对象，就是创建新的空的 Excel 文件。
wb = openpyxl.Workbook()
# wb.active 就是获取这个工作薄的活动表，通常就是第一个工作簿，也就是我们在上面的图片中看到的 sheet1。
sheet = wb.active
# 可以用 .title 给工作表重命名。现在第一个工作表的名称就会由原来默认的 “sheet1” 改为 "kaikeba"。
sheet.title = '开课吧'
# 向单个单元格写入数据
sheet['A1'] = '学科'
sheet['b1']='成绩'
score1 = ['数学', 95]
score2=['英语',90]
# 写入整行的数据，变量类型是一个列表
sheet.append(score1)
sheet.append(score2)
# 保存修改的 Excel
wb.save('1415.xlsx')
# 关闭 Excel
wb.close()