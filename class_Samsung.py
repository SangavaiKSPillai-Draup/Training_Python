from class_Mobile import Mobile


class Samsung(Mobile):
    manufacturer = "Samsung Inc"

    def __init__(self):
        super().__init__()
        self.name = " "
        self.series1 = " "

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


sam1 = Samsung()
sam1.name = input("Enter name of Samsung mobile")
sam1.series = input("Enter series of Samsung mobile")
print("Samsung Mobile Details:\n", sam1)
