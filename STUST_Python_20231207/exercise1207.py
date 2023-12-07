class Sports:
    def __init__(self,name):
        self._name = name

    @property
    def sports_name(self):
        return self._name

    @sports_name.setter
    def sport_name(self, value):
        self.name = value

    def practice(self):
        print("Doing sport practice")




class landsports(Sports):
    def __init__(self, name, field):
        super().__init__(name)
        self._field = field

    @property
    def landsports_field(self):
        return self._field

    def practice(self):
        print("Doing land sport practice")

class Watersports(Sports):
    def __init__(self, name, activity):
        super().__init__(name)
        self._activity = activity

    @property
    def Watersports_activity(self):
        return self._activity

    def practice(self):
        print("Doing water sport practice")


if __name__ == "__main__":

    baseball = landsports("baseball", "baseball.field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    baseball.practice()

    water_skiing = Watersports("water_skiing", "Strap on your skis and fly across the water")
    print(water_skiing.sports_name)
    print(water_skiing._activity)

    