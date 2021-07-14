from class_Mobile import Mobile


class OnePlus(Mobile):
    manufacturer = "BBK Electronics"

    def __init__(self):
        super().__init__()
        self.name = " "


plus1 = OnePlus()
plus1.name = input("Enter name of OnePlus mobile")
print("Object Details:\n", plus1)