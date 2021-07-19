from class_Smartphone import Smartphone


class Oppo(Smartphone):
    manufacturer = "BBK Electronics"
    series_list = ["Find X", "Reno", "F", "A"]

    def __init__(self):
        super().__init__()
        self.name = " "
        self.series1 = " "
        self.battery_ah = 0

    @property
    def series(self):
        return self.series1

    @series.setter
    def series(self, ser1):
        if ser1 not in Oppo.series_list:
            raise ValueError("Series mentioned is incorrect")
        self.series1 = ser1

    @series.deleter
    def series(self):
        del self.series1

    @series.getter
    def series(self):
        print("Getter is called")
        return self.series1

    @staticmethod
    def print_manufacturer():
        return Oppo.manufacturer

    def __str__(self):
        str1 = super().__str__()
        str1 += "\nMobile Series: " + self.series
        return str1

    def determine_cost(self):
        self.battery_ah = int(input("Enter the Mega Ampere-hours(MaH) value of battery: "))
        val = self.battery_ah
        if val<100:
            raise ValueError("Improper value for battery MAH")
        if val <= 2000:
            return 15000.00
        elif 2000 < val <= 4500:
            return 40000.00
        else:
            return 70000.00


ppo1 = Oppo()
ppo1.name = input("Enter name of Oppo mobile")
ppo1.series = input("Enter series of Oppo mobile")
print("Oppo Mobile Details:\n", ppo1)
print("Determine the cost of your phone, by entering the following: ")
cost = ppo1.determine_cost()
print("The cost of your phone: ",cost)

