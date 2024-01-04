#炸雞類別
class friedchicken:
#種類,九層塔,辣,胡椒,多少
    def __init__(self,type,basil,spicy,pepper,howmuch):
        self.type=type
        self.basil=basil
        self.spicy=spicy
        self.pepper=pepper
        self.howmuch=howmuch

    def Addingmaterials(self):
        print("type:",self.type)
        print("basil yes or not:",self.basil)

    def taste(self):
        if self.spicy == "no" and self.pepper == "no" : 
            print("taste:both not")
        elif self.spicy == "yes" and self.pepper == "no":
            print("taste:spicy")
        elif self.pepper == "yes" and self.spicy == "no" :
            print("taste:pepper")
        else:
            print("taste:both")
    def amount(self):
        print("amount:",self.howmuch)


ch1 = friedchicken("wing","yes","yes","yes",100)
ch1.Addingmaterials()
ch1.taste()
ch1.amount()

ch1 = friedchicken("drumstick","no","no","yes",50)
ch1.Addingmaterials()
ch1.taste()
ch1.amount()

ch1 = friedchicken("feet","no","yes","no",100)
ch1.Addingmaterials()
ch1.taste()
ch1.amount()

ch1 = friedchicken("skin","yes","no","no",150)
ch1.Addingmaterials()
ch1.taste()
ch1.amount()