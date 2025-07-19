class a:

    def showmy(self):
        print('come to dubai a')
#
# class b(a):
#
#      def display(self):
#         print('come to dubai b')

class b:
    def display(self):
        print('come to dubai b')

class c(a,b):
         pass

obj = b()
# obj.showmy()
obj.display()


obj2 = c()
obj2.display()
obj2.showmy()


# class parent:
#     def __init__(self):
#         print('I am parent')
#
# class child(parent):
#     def __int__(self): # here ony child run not parent unless , parent constructor call manually
#         print("i am child")
#
# c = child()



class parent:
    def __init__(self):
        print('I am parent')

class child(parent):
    def __init__(self):
        print("i am  child")
        super().__init__() # it is used to call the parent constructor

c = child()





























