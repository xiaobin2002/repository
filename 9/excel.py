import  openpyxl
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet.title='2216'
# sheet['A1']='姓名'
# sheet['b1']='年龄'
# row1=['金毛狮王',27,0]
# row2=['青翼蝠王',23,0]
# row3=['紫衫龙王',18,0]
# row4=['白眉鹰王',24,0]
# sheet.append(row1)
# sheet.append(row2)
# sheet.append(row3)
# sheet.append(row4)
# wb.save('2216k4.xlsx')
# wb.close()
wb=openpyxl.load_workbook('2216k4.xlsx')
print(wb['2216']['a6'].value)