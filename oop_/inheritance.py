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




























