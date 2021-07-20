"""
A hypothetical mobile phone brand, that has the features of Oppo and Samsung.
This class is implemented to understand the concept of Method Resolution Order,
and Class Decorators
"""

from class_Samsung import Samsung
from class_Oppo import Oppo


def sop_deco(cls):
    print("\nDecorating SOP class with SOP_DECO")
    members = vars(cls)
    for name, member in members.items():
        print(name, member)
    return cls


@sop_deco
class SOP(Samsung, Oppo):
    manufacturer = "ABC Mobiles"
    series_list = ["Find S", "Find F", "Galaxy Reno"]

    def __init__(self):
        super().__init__()
        self.name = input("\nEnter name of your mobile: ")


phone1 = SOP()
'''
phone1.series = input(
    "Enter series of your mobile: ")  # Output shows value error corresponding to Samsung class's @series.setter method.
'''
print("\nMethod Resolution Order: \n", SOP.__mro__)
