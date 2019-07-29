''' 3.	Write a program to read the file Result.xlsx which has the following information about students: 
a.	USN
b.	NAME
c.	Subject information: INTERNAL, EXTERNAL (scores)
d.	TOTAL
e.	Grade
f.	Credit of each subject

Find the SGPA of each student using the following formula:

SGPA (Si) = Σ(Ci x Gi) / Σci

where Ci is the number of credits of the ith course and Gi is the Grade Point scored by the student in that ith course. The table below displays the method to calculate the Grade Point.
'''
from openpyxl import Workbook
import openpyxl as pyxl

l_s_map = {"S":9,"S+":10,"O":10,"A":8,"B":7,"C":6,"D":5,"E":4,"F":6}
class Student:
    def __init__(self,usn,name):
        self.usn = usn
        self.name = name 
        self.subjects = []

    def show_sgpa_info(self):
        g_c = 0
        s_c = 0
        for s in self.subjects:
            g_c += s["C"] * l_s_map[s["G"]]
            s_c += s["C"]
        si = g_c / s_c
        print(f"NAME:{self.name} SCPA:{si}")
students = []
wb = pyxl.load_workbook("Result.xlsx")
sheet = wb.active
for row in sheet.iter_rows(min_row = 3,min_col = 2,max_col = 13):
    if row:
        data = [c.value for c in row]
        stu= data [:2]
        sub_1 = data[5:7]
        sub_2 = data[-2:]
        student =Student(*stu)
        student.subjects.append({"C":sub_1[0],"G":sub_1[1]})
        student.subjects.append({"C":sub_2[0],"G":sub_2[1]})
        students.append(student)

for s in students:
    s.show_sgpa_info()
    




