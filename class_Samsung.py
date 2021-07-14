from class_Mobile import Mobile


class Samsung(Mobile):
    manufacturer = "Samsung Inc"

    def __init__(self):
        super().__init__()
        self.name = " "


sam1 = Samsung()
sam1.name = input("Enter name of Samsung mobile")
print("Object Details:\n", sam1)




