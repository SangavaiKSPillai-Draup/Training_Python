from class_Smartphone import Smartphone


class Oppo(Smartphone):
    manufacturer = "BBK Electronics"
    series_list = ["Find X", "Reno", "F", "A"]

    def __init__(self):
        super().__init__()
        self.name = " "
        self.series1 = " "
        self.battery_ah = 0
        self.camera_mp = 0

    @property
    def series(self):
        return self.series1

    @series.setter
    def series(self, ser1):
        if ser1 not in Oppo.series_list:
            raise ValueError("Series mentioned is incorrect. It should be one of", Oppo.series_list)
        self.series1 = ser1

    @series.deleter
    def series(self):
        del self.series1

    @series.getter
    def series(self):
        # print("Getter is called")
        return self.series1

    @staticmethod
    def print_manufacturer():
        return Oppo.manufacturer

    def __str__(self):
        str1 = super().__str__()
        str1 += "\nMobile Series: " + self.series
        return str1

    @classmethod
    def get_Series_List(cls):
        return cls.series_list

    def determine_cost(self, *args):
        # self.battery_ah = int(input("Enter the Mega Ampere-hours(MaH) value of battery: "))
        val = args[0]
        if val < 900:
            if val < 0:
                raise ValueError("Improper value for Camera MP")
            if val <= 48:
                return 10000.00
            elif 48 <= val <= 64:
                return 30000.00
            else:
                return 70000.00
        elif val <= 2000:
            return 15000.00
        elif 2000 < val <= 4500:
            return 40000.00
        else:
            return 70000.00

    def findSeries(self):
        mob_series = [elem for elem in self.series_list if elem in self.name]
        if len(mob_series) == 0:
            raise ValueError("Can't find series for mobile: ", self.name)
        self.series = mob_series[0]
        return self


"""
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
"""
