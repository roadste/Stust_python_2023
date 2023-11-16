class Person:
    def __init__ (self ,name, age):
       self.name = name
       self.age = age


    def __str__(self):
        return f"Name : {self.name}\nAge = {self.age}"

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John" ,36)
p2 = Person("Jennifer" ,25)

print(p1.name)
print(p1.age)
print(p1)
print(p2)
p1.myfunc()

'參數 邊 長 寬 半徑'
'此類別用來求面積'
class Myshape:
    def __init__ (self, side, length, width,radius):
        self.side = side
        self.length = length
        self.width = width
        self.radius = radius
    
    def rectangle(self):
        print("長方面積 = ",self.length*self.width)
    def square(self):
        print("正方面積 = ",self.side*self.side)
    def round(self):
        print("圓面積 = ",pow(self.radius,2)*3.14)

p1 = Myshape(2,2,3,2)

p1.rectangle()
p1.square()
p1.round()