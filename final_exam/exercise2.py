#類別飲料店員工
class Beverageshopemployer:
    def __init__(self,name,Seniority,time):
        self.name = name
        self.Seniority = Seniority
        self.time = time

    def searchname(self):
        print(self.name)

    def seniority(self):
        print(self.Seniority)

    def worktime(self):
        print(self.time)

    def salary(self,monthlysalary):
        monthlysalary = self.time * 200
        print(monthlysalary)

    def overtime(self,new_overtime):
        new_overtime = self.time - 240
        print(new_overtime)