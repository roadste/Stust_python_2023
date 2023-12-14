class Student:
    def __init__(self,name ,id ,major):
        self._name = name
        self._id = id
        self._major = major

    def addCourse(self,course):
        self.course = course
        print("name:",self._name," addCourse:",self.course)

    def WithdrawCourse(self,course):
        print("name:"," WithdrawCourse",self._name,course)

    def search(self):
        print("search result:",self.course)

   
st1 = Student("hank",5210,"資工")
st1.addCourse("c語言")
st1.search()
