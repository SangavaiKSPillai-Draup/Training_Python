import random
from abc import abstractmethod

min_range = 1
max_range = 30


class Smartphone:
    """
    The base class of Smartphones
    """

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
        # print("Getter is called")
        return self.name1

    def __str__(self):
        str1 = "Smartphone ID: " + str(self._id)  # type: str
        str1 += "\nSmartphone Name: " + self.name1
        return str1

    @abstractmethod
    def determine_cost(self):
        """
        Abstract method that is used to calculate the cost of
        smartphone
        """
        pass


"""
sma1 = Smartphone()
print("Creating an object")
sma1.name = input("Enter a smartphone name: ")
print("Smartphone Details\n", mob1)
"""
