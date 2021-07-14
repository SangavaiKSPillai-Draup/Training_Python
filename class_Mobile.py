import random

min_range = 1
max_range = 30


class Mobile:

    def __init__(self):
        self._id = random.randint(min_range, max_range)
        self.name1 = " "

    @property
    def name(self):
        return self.name1

    @name.setter
    def name(self, nam1):
        self.name1 = nam1

    @name.deleter
    def name(self):
        del self.name1

    @name.getter
    def name(self):
        print("Getter is called")
        return self.name1

    def __str__(self):
        str1 = "Mobile ID: " + str(self._id)  # type: str
        str1 += "\nMobile Name: " + self.name1
        return str1


mob1 = Mobile()
print("Creating an object")
mob1.name = input("Enter a mobile name: ")
print("Object Details\n", mob1)
