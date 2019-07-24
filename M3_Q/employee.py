class Employee:
    def __init__(self,empno,ename,qualification,salary,dept_name):
        self.empno = empno
        self.ename =ename
        self.qualification = qualification
        self.salary =salary
        self.dept_name = dept_name
    def showInfo(self):
        print(f"{self.empno}-{self.ename}-{self.qualification}-{self.salary}-{self.dept_name}")
    
    def increment_salary(self,inc_amount):
        self.salary += inc_amount
        print(f"{self.ename} salary after increment :{self.salary}")