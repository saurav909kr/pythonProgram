class DemoClass:
    a=10

    def sumvalue(self):
        print(20+22)
        c = self.a * self.a
        print(c)

    def name(self,c,d):
        print("welcome to my hoood",c+d)

obj = DemoClass()
obj1 = DemoClass()
print(obj.a)
print(obj1.a)

obj.sumvalue()

obj.name(99,55)


#-------constructor----


class DemoClass:
    a=10

    def __init__(self):
          print("welcome to my home")

    def sumvalue(self):
            print(20 + 22)
            c = self.a * self.a
            print(c)

    def name(self, c, d):
            print(c + d)

obj = DemoClass()
obj.sumvalue()
obj.name(99,55)


class student():
     def __init__(self,name,branch):
      self.branch = branch
      self.name = name
     #name  = name
    #branch = branch

     # def __str__(self):
     #     return f'{self.name},{self.branch}'


std = student("saurabh","Data Science")
# print(std)
#print(std)
# print(std.name)
# print(std.branch)

# del std.branch
# print(std.branch)
# del std
# print(std)







