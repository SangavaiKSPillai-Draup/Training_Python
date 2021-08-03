from class_Smartphone import Smartphone


class Samsung(Smartphone):
    manufacturer = "Samsung Inc"
    series_list = ["Galaxy Z", "Galaxy S", "Galaxy A", "Galaxy M", "Galaxy F"]

    def __init__(self):
        super().__init__()
        self.name = " "
        self.series1 = " "
        self.camera_mp = 0
        self.battery_ah = 0

    @property
    def series(self):
        return self.series1

    @series.setter
    def series(self, ser1):
        if ser1 not in Samsung.series_list:
            raise ValueError("Series mentioned is incorrect. It should be one of", Samsung.series_list)
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
        return Samsung.manufacturer

    def __str__(self):
        str1 = super().__str__()
        str1 += "\nSmartphone Series: " + self.series
        return str1

    def determine_cost(self):
        self.camera_mp = int(input("Enter Megapixel value of camera: "))
        val = self.camera_mp
        if val < 0:
            raise ValueError("Improper value for Camera MP")
        if val <= 48:
            return 10000.00
        elif 48 <= val <= 64:
            return 30000.00
        else:
            return 70000.00

    def findSeries(self):
        mob_series = [elem for elem in self.series_list if elem in self.name]
        if len(mob_series) == 0:
            raise ValueError("Can't find series for mobile: ", self.name)
        self.series = mob_series[0]
        return self

    @classmethod
    def get_Series_List(cls):
        return cls.series_list


"""
sam1 = Samsung()
sam1.name = input("Enter name of Samsung mobile")
sam1.series = input("Enter series of Samsung mobile")
print("Samsung Mobile Details:\n", sam1)
print("Determine the cost of your phone, by entering the following: ")
cost = sam1.determine_cost()
print("The cost of your mobile is: ", cost)
"""
