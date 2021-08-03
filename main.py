from dataclass_Mobile import Mobile
from class_Samsung import Samsung
from class_Oppo import Oppo

sam1 = Samsung()
sam1.name = input("Enter name of Samsung mobile")
sam1.series = input("Enter series of Samsung mobile")
print("Samsung Mobile Details:\n", sam1)
print("Determine the cost of your phone, by entering the following: ")
cost = sam1.determine_cost()
print("The cost of your mobile is: ", cost)

ppo1 = Oppo()
ppo1.name = input("Enter name of Oppo mobile")
ppo1.series = input("Enter series of Oppo mobile")
print("Oppo Mobile Details:", ppo1)
battery_ah = int(input("Enter the Mega Ampere-hours(MaH) value of battery: "))
camera_mp = int(input("Enter Megapixel value of camera: "))
# print("Determine the cost of your phone, by entering the following: ")
cost = ppo1.determine_cost(battery_ah)
print("The cost of your phone (as per battery): ", cost)
cost = ppo1.determine_cost(camera_mp)
print("The cost of your phone (as per camera megapixel)", cost)

m1 = Mobile.readFile()


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

    return samsung_mobile, oppo_mobile


sam_list, oppo_list = findSeries(m1)
"""
print("Samsung Mobiles List: ")
for item in sam_list:
    print(item)
print("Oppo Mobiles List: ")
for item in oppo_list:
    print(item)
"""

m_series = []
for item in sam_list:
    m2 = Mobile()
    m2.writeData(item.name, item.manufacturer, item.camera_mp, item.battery_ah, item.series, '')
    m_series.append(m2)

for item in oppo_list:
    m2 = Mobile()
    m2.writeData(item.name, item.manufacturer, item.camera_mp, item.battery_ah, item.series, '')
    m_series.append(m2)

for item in m_series:
    print(item)

# Mobile.writeFile(m_series)
'''
nam, manf, camm, batt = Mobile.getUserInput()
m_obj = Mobile()
m_obj.writeData(nam, manf, camm, batt, '', '')
# print(m_obj)
m_obj.updateFile()
'''
# Mobile.deleteRowInFile()
