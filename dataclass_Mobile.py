"""
A dataclass is now created here to store information regarding mobiles
"""

from dataclasses import dataclass
import csv


@dataclass
class Mobile:
    id: str
    name: str
    series: str
    camera_mp: int
    battery_ah: int
    cost: float

    def __init__(self):
        self.id = ''
        self.name = ''
        self.series = ''
        self.camera_mp = 0
        self.battery_ah = 0


m1 = Mobile()
f1 = open("smartphone_data.csv", 'r', encoding='UTF-8')
data = csv.reader(f1)
data = list(data)
# data[0][0] = 'Name'
for row in data:
    print(row)
f1.close()
'''
f2 = open("smartphone_data.csv", 'w', newline='', encoding='UTF-8')
writer = csv.writer(f2)
writer.writerows(data)
f2.close()
'''

