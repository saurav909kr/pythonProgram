w = "Mistake are proof that you are trying" # gap is also counting in index

print("lent of w :", len(w))
print(w[2])
print(w[-1])

print(w.index("k"))
print(w.find("k"))

print( w[0:6])
print( w[0::2])

print("slice from back :", w[:: -1])
print("slice from back :", w[-1:-4: -1])

print(w[7::-1])

print(w[-10: -1: 2])
print("reverse string",w[-1::-1])

#---------------------

name = "saurabh"
length = len(name)

print("character | +index | -index")
print("-----------------------------")
for i,ch in enumerate(name):
    pos_index = i
    neg_index  = i - length
    print(f"    {ch}     |     {pos_index:2}    |     {neg_index:2}    ")

#----------------------

w = "abc"
for x, c in enumerate(w): # it giv index to x and cha to c
    print(x, c)

#----------------------

l = len(w)

for a in range(l):
    print(w[a])

for a in range(l-1,-1,-1):
    print(w[a],end=",") # end is used to prevent default new line

#----------------------------

str_1 = "local"

for a in str_1:
    print(a)

#---------------------------



