#-----function define
def showdata():
    print("welcome to my hood")

showdata()

#----function with argument
def plus(a,b):
    print(a+b)

plus(20,50)

#--- function with return

def mutiplty(a,b):
    c = a*b
    return c

output = mutiplty(22,55)
print(output)

#------arbitrary argument

def language(*lang):
    print("My fav language is :" + lang[1])

language("c",'python','java','rust')

#-----keyboard argument

def movie(movie1,movie12,movie3):
    print("movie i watch most :" + movie3)

movie(movie12= "radha",movie1="kgf", movie3="malik")

#------------------------------------------------------------------
def movie(**movie):
    print("movie i watch most :" + movie["movie3"])

movie(movie12= "radha",movie1="kgf", movie3="malik")

#-----------------------------------------------------------------

def myfriend(dost):
    for x in dost:
        print(x)

friend = ['abhijeet','aditya','ritik','sandeep']
myfriend(friend)

#-----------------------------------------------------------------

def function(s, /): #only positional  argument
      print(s)

function(5)

#--------------------------------------------------------
def function(s, /):
    print(s)

#function(s=5) #give error

#------------------------------------------------------
def functionnn(*, s): #only keyword argument
    print(s)

functionnn(s=9)

#-----------------------------------------------------------
def myfunction(a, b, /, *, c, d): #positional and keyword both argument
  print(a + b + c + d)

myfunction(5, 6, c = 99, d = 77)

#-------------recursion
def recursion(m):
    if(m < 16):
        result = m + recursion(m+1)
        print(result)
    else:
       result = 0
    return result

recursion(10)








