class calculation:
    def find_multi(self, x = None, y = None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothind to calculate")

obj = calculation()
obj.find_multi()
obj.find_multi(33)
obj.find_multi(10,55)

