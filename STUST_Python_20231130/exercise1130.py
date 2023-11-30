class Student:

    def __init__(self) -> None:
        pass
    #姓名,學校,科系,系主任,學分,成績,學號,通訊地址
    def __init__(self ,name ,school ,major ,Director ,credit ,score ,id ,address):
        self.name = name
        self.school = school
        self.major = major
        self.Director = Director
        self.credit = credit
        self.score = score
        self.id = id
        self.address = address

    #設置姓名和讀取姓名
    def setname(self,new_name):
        self.name = new_name

    def Getname(self):
        return self.name

    #設置學校和讀取學校
    def Setschool(self,new_school):
        self.school = new_school

    def Getschool(self):
        return self.school

    #設置科系讀取科系
    def Setmajor(self,new_major):
        self.major = new_major

    def Getmajor(self):
        return self.major

    #設置系主任讀取系主任
    def GetDirector(self,new_Director):
        self.Director = new_Director

    def GetDirector(self):
        return self.Director

    #設置學分讀取學分
    def Setcredit(self,new_credit):
        self.credit = new_credit

    def Getcredit(self):
        return self.credit

    #設置成績讀取成績
    def Setscore(self,new_score):
        self.score = new_score

    def Getscore(self):
        return self.score

    #設置學號讀取學號
    def Setid(self,new_id):
        self.id = new_id

    def Getid(self):
        return self.id

    #設置通訊地址讀取通訊地址
    def Setaddress(self,new_address):
        self.address = new_address

    def Getaddress(self):
        return self.address


st1 = Student("hi","stust","computer","hello",20,60,123456,"ttttt")
print(st1.Getmajor())
print(st1.Getaddress())
