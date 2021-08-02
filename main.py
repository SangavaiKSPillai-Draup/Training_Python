import csv
from dataclass_Mobile import Mobile
from class_Samsung import Samsung
from class_Oppo import Oppo

m1 = []
f1 = open("smartphone_data.csv", 'r', encoding='UTF-8')
data = csv.reader(f1)
i = next(data)
data = list(data)
# data[0][0] = 'Name'
name_column = 0
man_column = 1
camera_mp_column = 2
battery_ah_column = 3
for row in data:
    # print(row
    m2 = Mobile()
    m2.writeData(row[name_column], row[man_column], row[camera_mp_column], row[battery_ah_column])
    m1.append(m2)
f1.close()
'''
print("List of Mobile Class Objects: ")
for item in m1:
    print(item)
'''

'''
Finding series of the mobiles in the dataset
'''


def findSeries(mobile_list):
    """
    for ele in mobile_list:
        print(ele)
    """
    samsung_series_list = Samsung.get_Series_List()
    oppo_series_list = Oppo.get_Series_List()
    samsung_mobile = []
    oppo_mobile = []
    for mob in mobile_list:
        # print(mob.manufacturer)
        m_name = mob.name
        man_name = mob.manufacturer
        if man_name == Samsung.manufacturer:
            print(mob.name)
            mob_series = [elem for elem in samsung_series_list if elem in m_name]
            if len(mob_series) == 0:
                raise ValueError("Can't find series for mobile: ", mob.name)
            sm1 = Samsung()
            sm1.name = m_name
            sm1.series = mob_series[0]
            sm1.camera_mp = mob.camera_mp
            samsung_mobile.append(sm1)
        if man_name == Oppo.manufacturer:
            mob_series = [elem for elem in oppo_series_list if elem in m_name]
            if len(mob_series) == 0:
                raise ValueError("Can't find series for mobile: ", mob.name)
            op1 = Oppo()
            op1.name = mob.name
            op1.series = mob_series[0]
            op1.camera_mp = mob.camera_mp
            op1.battery_ah = mob.battery_ah
            oppo_mobile.append(op1)

    return samsung_mobile, oppo_mobile


sam_list, oppo_list = findSeries(m1)
print("Samsung Mobiles List: ")
for item in sam_list:
    print(item)
print("Oppo Mobiles List: ")
for item in oppo_list:
    print(item)
