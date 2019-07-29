from openpyxl import Workbook
wb =Workbook()
sheet = wb.active  #active means current sheet
data = [
    ('id','wname','year','status','company'),
    (1001,"python",2019,1,"hearizen"),
    (1002,"introduction to web",2018,1,"spaneos")

]

for row in data:
    sheet.append(row)
wb.save("ws4.xlsx")