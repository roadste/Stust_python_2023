class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department, emp_hour):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        self.emp_hour = emp_hour

    def calculate_emp_salary(self):
        overhour=0
        overpay = 0
        pay = 0

        if self.emp_hour > 50:
             overhour= self.emp_hour - 50
             overpay = 50 * self.emp_salary + (overhour * (self.emp_salary/50))
             print(overpay)

        else :
            pay = self.emp_salary * self.emp_hour
            print(pay)

        #print(self.emp_salary)

    def emp_assign_department(self,new_department):
        self.emp_department = new_department
        
    def print_employee_details(self):
        print(self.emp_department)
        print(self.emp_id,self.emp_name)

    
e1 = Employee ("E7876","亞當",50000,"會計",40)
e1.print_employee_details()
e1.emp_assign_department("研究")




