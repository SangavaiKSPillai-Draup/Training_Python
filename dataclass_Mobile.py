"""
A dataclass is now created here to store information regarding mobiles
"""
import csv
import json
from dataclasses import dataclass


@dataclass
class Mobile:
    name: str
    series: str
    camera_mp: int
    battery_ah: int
    cost: float
    manufacturer: str

    def __init__(self):
        self.name = ''
        self.manufacturer = ''
        self.camera_mp = 0
        self.battery_ah = 0
        self.cost = 0
        self.series = ''

    def writeData(self, name, manfac, camera_mp, battery_ah, series, cost):
        self.name = name
        self.manufacturer = manfac
        self.camera_mp = camera_mp
        self.battery_ah = battery_ah
        self.series = series
        self.cost = cost

    @classmethod
    def getUserInput(cls):
        nam = input("Enter phone name: ")
        manf = input("Enter manufacturer of phone: ")
        cam_mp = int(input("Enter megapixel value for camera: "))
        batt_ah = int(input("Enter mAH value of battery: "))
        return nam, manf, cam_mp, batt_ah

    def __str__(self):
        str1 = ''
        if self.name != '':
            str1 = "Name: " + self.name
        if self.manufacturer != '':
            str1 += "\nManufacturer: " + self.manufacturer
        if self.camera_mp != '' and self.camera_mp != 0:
            str1 += "\nCamera MP: " + str(self.camera_mp)
        if self.battery_ah != '' and self.battery_ah != 0:
            str1 += "\nBattery mAH: " + str(self.battery_ah)
        if self.series != '':
            str1 += "\nSeries: " + self.series
        if self.cost != '' and self.cost != 0:
            str1 += "\nCost: " + str(self.cost)
        return str1

    @classmethod
    def writeFile(cls, mobile_list):
        # f1 = open("smartphone_data.csv", 'w', encoding='UTF-8', newline='')
        header = ["Name", "Manufacturer", "Camera_mp", "Battery_ah", "Series", "Cost"]
        # it1 = iter(header)
        m1 = []
        for ele in mobile_list:
            it1 = iter(header)
            it2 = iter([ele.name, ele.manufacturer, ele.camera_mp, ele.battery_ah, ele.series, ele.cost])
            dict1 = dict(zip(it1, it2))
            m1.append(dict1)
            # w1.writerow([item.name, item.manufacturer, item.camera_mp, item.battery_ah, item.series, item.cost])
        f1 = open("smartphone_data.json", 'w', encoding='UTF-8')
        jsonString = json.dumps(m1, indent=2)
        f1.write(jsonString)
        f1.close()
        # print("File Written\n")
        # f1.close()

    @classmethod
    def readFile(cls):
        m1 = []
        f1 = open("smartphone_data.json", 'r', encoding='UTF-8')
        data = json.load(f1)
        series_column = 4
        cost_column = 5
        k1 = 'Name'
        k2 = 'Manufacturer'
        k3 = 'Camera_mp'
        k4 = 'Battery_ah'
        k5 = 'Series'
        k6 = 'Cost'
        for item in data:
            m2 = Mobile()
            if len(item.keys()) == series_column:
                m2.writeData(item[k1], item[k2], item[k3], item[k4], '', '')
            elif len(item.keys()) == cost_column:
                m2.writeData(item[k1], item[k2], item[k3], item[k4], item[k5], '')
            else:
                m2.writeData(item[k1], item[k2], item[k3], item[k4], item[k5], item[k6])
            m1.append(m2)
        f1.close()
        return m1

    def updateFile(self):
        header = ["Name", "Manufacturer", "Camera_mp", "Battery_ah", "Series", "Cost"]
        it1 = iter(header)
        it2 = iter([self.name, self.manufacturer, self.camera_mp, self.battery_ah, self.series, self.cost])
        dict1 = dict(zip(it1, it2))
        with open("smartphone_data.json", "r+", encoding='UTF-8') as file:
            data = json.load(file)
            data.append(dict1)
            file.seek(0)
            jsonString = json.dumps(data, indent=2)
            file.write(jsonString)
            print("File updated")
        '''
        f1 = open("smartphone_data.csv", 'a', encoding='UTF-8')
        w1 = csv.writer(f1)
        w1.writerow([self.name, self.manufacturer, self.camera_mp, self.battery_ah, self.series, self.cost])
        f1.close()
        '''

    @classmethod
    def deleteRowInFile(cls):
        m1 = Mobile.readFile()
        name = input("Enter name of Phone which has to be deleted from file: ")
        index = [index for index in range(len(m1)) if m1[index].name == name]
        if len(index) == 0:
            raise ValueError("No such phone name can be found")
        del m1[index[0]]
        Mobile.writeFile(m1)


# m1 = Mobile.readFile()
# Mobile.writeFile(m1)
'''
nam, manf, camm, batt = Mobile.getUserInput()
m_obj = Mobile()
m_obj.writeData(nam, manf, camm, batt, '', '')
m_obj.updateFile()
'''
Mobile.deleteRowInFile()
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
