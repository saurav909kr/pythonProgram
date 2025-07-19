class student:
    def display(self, name=""):
        print("my name is"+" "+name)

obj = student()
obj.display()
obj.display("ravi")

#----------------------concept of over-riding--------------

class parent:
    def display(self):
        print("welcome to parenthood")

class child(parent):
       def display(self):
           super().display() # call parent method
           print("welcont to childhood") # it ovr write parent method because method is same

obj = child()
obj.display()

#------------------------------------------------------------------------





















