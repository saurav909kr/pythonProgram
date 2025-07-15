# import module
# print(module.sum(10,20))

# import module as m
# print(m.sum(22,34))


# from module import sum     #--- you can use only sum function not another
# print(sum(24,76))


# from module import sum, mul   #-- here you can use only sum and mul
# print(sum(2,5))
# print(mul(8,5))


# from module import *      #----- by using all * brought all the function
# print(sum(2,56))
# print(mul(2,9))


#---------------------------------------------------------------------------------------------------------
import math

x = 12.4
y = 14
l = [30,55,37,80,99,4]

print(math.ceil(x), math.ceil(y))

print(math.floor(x),math.floor(y))

print(math.fsum(l))

print(math.sqrt(25))

a = 10
b = -13
print(math.fabs(a),math.fabs(b))

x = 8
y = -120
print(math.factorial(x))
# print(math.factorial(y))    #negative number give error

#--------------------------------------------------------------------------------------------

import random

n = random.randint(2,8)    #inclue 2 and 8 also
print(n)

n1 = random.randrange(3,9)   # include only 3 not 9
print(n1)

n2 = random.choice(l)
print("choice",n2)

n3 = random.random()
print(n3)

random.shuffle(l)
print(l)

n5 = random.uniform(3,7)
print(n5)

#---------------------------------------------------------------------------------------------------------

import datetime

b1 = datetime.datetime.now()
print(b1)

b2 = b1.strftime("%Y-%B-%d")
print(b2)


