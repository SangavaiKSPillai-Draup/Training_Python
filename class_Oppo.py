from class_Mobile import Mobile


class Oppo(Mobile):
    manufacturer = "BBK Electronics"

    def __init__(self):
        super().__init__()
        self.name = " "
        self.series = " "

    @property
    def series(self):
        return self.series1

    @series.setter
    def series(self, ser1):
        self.series1 = ser1

    @series.deleter
    def series(self):
        del self.series1

    @series.getter
    def series(self):
        print("Getter is called")
        return self.series1

    def __str__(self):
        str1 = super().__str__()
        str1 += "\nMobile Series: " + self.series;
        return str1


ppo1 = Oppo()
ppo1.name = input("Enter name of Oppo mobile")
ppo1.series = input("Enter series of Oppo mobile")
print("Oppo Mobile Details:\n", ppo1)
