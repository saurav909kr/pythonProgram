from traceback import print_tb


class bikeshop:
    def __init__(self,stock):
        self.stock = stock
    def displayBike(self):
        print("Total number of bike available Bike :", self.stock)
    def bikeOnRent(self,quantity):
        if quantity <= 0:
            print("Enter the number greater than zero")
        elif quantity > self.stock:
            print("Sorry! please enter the value less than stock ")
        else:
            print("Total price :",quantity*100)
            print("Total bike available :" ,self.stock-quantity)

while True:
    obj = bikeshop(100)
    userChoice = int(input('''
    1.Display the stock 
    2.Bike for rent 
    3.Exit
    '''))
    if userChoice == 1:
        obj.displayBike()
    elif userChoice == 2:
        n = int(input("Enter the quantity ...."))
        obj.bikeOnRent(n)
    else:
        break





