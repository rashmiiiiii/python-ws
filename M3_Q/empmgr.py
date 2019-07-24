from employee import Employee
lst_emp = []
def load_emp():
    with open("emp.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata = data.strip("\n").split(",")
            empno = int(edata[0])
            ename = edata[1]
            qualification = edata[2]
            salary = int(edata[3])
            dept_name = edata[4]
            emp = Employee(empno,ename,qualification,salary,dept_name)
            lst_emp.append(emp)
        print(f"total employees count {len(lst_emp)}")

def showDeptName():
    dnames = set(map(lambda emp:emp.dept_name,lst_emp))
    for name in dnames:
        print(name)
def showAllQualifications():
    qualifications = set(map(lambda emp:emp.qualification,lst_emp))
    for qual in qualifications:
        print(qual)

def maxSalaryEmp():
    sal = max(list(map(lambda emp : emp.salary,lst_emp)))
    max_sal = list(filter(lambda emp:emp.salary == sal,lst_emp))
    for ms in max_sal:
        ms.showInfo()
def showEmpCountByDeptName():
    s = list(set(map(lambda emp:emp.dept_name,lst_emp)))
    
def showTotalSalByDeptName():
    pass
def showEmpCountByQual():
    pass


load_emp()
print("all departments")
showDeptName()
print("all qualifications")
showAllQualifications()
print("maximum salary")
maxSalaryEmp()
'''emp_1 = Employee(1,"sunny","M.Tech",56000,"CS") #rogram to print the employee salary after the increment#
emp_2 = Employee(1,"Bunny","M.Tech",46000,"IS")
emp_1.showInfo()
emp_1.increment_salary(2000)
emp_1.showInfo()
emp_2.showInfo()'''