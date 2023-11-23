class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        

    def calculate_emp_salary(self,hour):
        overtime = 0

        if hour > 50:
            overtime = hour - 50
            self.salary = self.salary + (overtime * (self.salary / 50))
        else:
            self.salary = self.salary * (hour / 50)
 
            

    def emp_assign_department(self,new_department):
        self.department = new_department
        

    def print_employee_details(self):
        print("\nName: ", self.name)
        print("ID: ", self.id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("----------------------")

    
e1 = Employee ("E7876","ADAMS",50000,"ACCOUNTING")
e1.calculate_emp_salary(30)
e1.emp_assign_department("OPERATIONS")
e1.print_employee_details()

e2 = Employee ("E7499","JONES",45000,"RESEARCH")
e2.calculate_emp_salary(50)
e2.print_employee_details()

e3 = Employee ("E7900","MARTIN",50000,"SALES")
e3.calculate_emp_salary(0)
e3.print_employee_details()

e4 = Employee ("E7698","SMITH",55000,"OPERATIONS")
e4.calculate_emp_salary(60)
e4.emp_assign_department("SALES")
e4.print_employee_details()




