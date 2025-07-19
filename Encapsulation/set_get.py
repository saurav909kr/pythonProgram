# class student:
#     def __init__(self):
#         self.__name = ""
#         self.__branch = ""
#     def getname(self):
#         return  self.__name , self.__branch
#     def setname(self,name,branch):
#         self.__name = name
#         self.__branch = branch
#
# obj = student()
# obj.setname("arnav  rajarjun","data science")
# name = obj.getname()
# print(name)

#------------------------------------------------------------------------------------------------------------------------------

class person:
    __name = "Raj aryan" # using this (__) to make private  ,cannot use trough obj directly,
                         # but u get through constructor
    def __init__(self):
        print(self.__name)

        self.__display()
    def __display(self): # this class cannot get by outside , to can you should call the this method inside
        print("my name is raj arjun")

obj = person()
# obj.__display()
# print(obj.__name)





