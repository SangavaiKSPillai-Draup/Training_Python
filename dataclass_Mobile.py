"""
A dataclass is now created here to store information regarding mobiles
"""

from dataclasses import dataclass


@dataclass
class Mobile:
    name: str
    series: str
    camera_mp: int
    battery_ah: int
    cost: float

    def __init__(self):
        self.name = ''
        self.manufacturer = ''
        self.camera_mp = 0
        self.battery_ah = 0

    def writeData(self, name, manfac, camera_mp, battery_ah):
        self.name = name
        self.manufacturer = manfac
        self.camera_mp = camera_mp
        self.battery_ah = battery_ah

    def __str__(self):
        str1 = "Name: " + self.name
        str1 += "\nManufacturer: " + self.manufacturer
        str1 += "\nCamera MP: " + str(self.camera_mp)
        str1 += "\nBattery mAH: " + str(self.battery_ah)
        return str1


"""
m1 = []
f1 = open("smartphone_data.csv", 'r', encoding='UTF-8')
data = csv.reader(f1)
i = next(data)
data = list(data)
# data[0][0] = 'Name'

for row in data:
    print(row)
f1.close()
"""

'''
f2 = open("smartphone_data.csv", 'w', newline='', encoding='UTF-8')
writer = csv.writer(f2)
writer.writerows(data)
f2.close()
'''
