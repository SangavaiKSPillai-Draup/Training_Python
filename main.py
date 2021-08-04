from dataclass_Mobile import Mobile
from class_Samsung import Samsung
from class_Oppo import Oppo
import os

sam1 = Samsung()
sam1.name = input("Enter name of Samsung mobile: ")
sam1.series = input("Enter series of Samsung mobile: ")
print("Samsung Mobile Details:\n", sam1)
print("Determine the cost of your phone, by entering the following: ")
cost = sam1.determine_cost()
print("The cost of your mobile is: ", cost)

i = input("\n Press enter to continue ...")
# print("Press any key to continue: ")

ppo1 = Oppo()
ppo1.name = input("Enter name of Oppo mobile: ")
ppo1.series = input("Enter series of Oppo mobile: ")
print("Oppo Mobile Details:\n", ppo1)
battery_ah = int(input("Enter the Mega Ampere-hours(MaH) value of battery: "))
camera_mp = int(input("Enter Megapixel value of camera: "))
# print("Determine the cost of your phone, by entering the following: ")
cost = ppo1.determine_cost(battery_ah)
print("The cost of your phone (as per battery): ", cost)
cost = ppo1.determine_cost(camera_mp)
print("The cost of your phone (as per camera megapixel)", cost)

# os.system("\n read -p 'Press Enter to continue...' var")
i = input("\n Press Enter to continue ...")
# m1 = Mobile.readFile()


def findSeries(mobile_list):
    samsung_mobile = []
    oppo_mobile = []
    for mob in mobile_list:
        # print(mob.manufacturer)
        m_name = mob.name
        man_name = mob.manufacturer
        if man_name == Samsung.manufacturer:
            sm1 = Samsung()
            sm1.name = m_name
            sm1.camera_mp = mob.camera_mp
            sm1.battery_ah = mob.battery_ah
            sm1 = sm1.findSeries()
            samsung_mobile.append(sm1)
        if man_name == Oppo.manufacturer:
            op1 = Oppo()
            op1.name = mob.name
            op1.camera_mp = mob.camera_mp
            op1.battery_ah = mob.battery_ah
            op1 = op1.findSeries()
            oppo_mobile.append(op1)

    m_series = []
    for item in samsung_mobile:
        m2 = Mobile()
        m2.writeData(item.name, item.manufacturer, item.camera_mp, item.battery_ah, item.series, '')
        m_series.append(m2)

    for item in oppo_mobile:
        m2 = Mobile()
        m2.writeData(item.name, item.manufacturer, item.camera_mp, item.battery_ah, item.series, '')
        m_series.append(m2)

    return m_series


# m_series = findSeries(m1)
"""
print("Samsung Mobiles List: ")
for item in sam_list:
    print(item)
print("Oppo Mobiles List: ")
for item in oppo_list:
    print(item)
"""
'''
for item in m_series:
    print(item)
'''
# Mobile.writeFile(m_series)
'''
nam, manf, camm, batt = Mobile.getUserInput()
m_obj = Mobile()
m_obj.writeData(nam, manf, camm, batt, '', '')
# print(m_obj)
m_obj.updateFile()
'''
# Mobile.deleteRowInFile()
ch = 1
while True:
    print("\nMAIN MENU: ")
    print("1 - Read the contents of file: ")
    print("2 - Find the series of the mobile phone and write into the file: ")
    print("3 - Update a new row in the file: ")
    print("4 - Delete a row in the file: ")
    print("5 - Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        m1 = Mobile.readFile()
        for item in m1:
            print(item)
    elif ch == 2:
        m1 = Mobile.readFile()
        m_series = findSeries(m1)
        for item in m_series:
            print(item)
        Mobile.writeFile(m_series)
    elif ch == 3:
        nam, manf, camm, batt = Mobile.getUserInput()
        m_obj = Mobile()
        m_obj.writeData(nam, manf, camm, batt, '', '')
        # print(m_obj)
        m_obj.updateFile()
    elif ch == 4:
        Mobile.deleteRowInFile()
    elif ch == 5:
        break
    else:
        raise ValueError("Invalid Option")
