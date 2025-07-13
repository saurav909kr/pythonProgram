t = ('python',40 , 'rohan', 'cricket' ,45 , 40)

print(type(t))
print(t[1:4])
print(t[2])
print(t[-2])
print(t)
print(len(t))

if 40 in t:
    print('yes')

            #---------------Tuple iteration
for a in range(0,4):
    print(t[a])

print()

for b in t:
    print(b)

print()

i = 0
while i < len(t):
    print(t[i])
    i = i+1

             #-----------------tuple methods
t2 = (20,44,56,33,20,44,100)
s1 = ('suman', 'pintu', 'rohit', 'radha')

m = min(t2)
print("min is :",m)

n = max(t2)
print("max is :",n)

m = min(s1)
print("min is :",m)

n = max(s1)
print("max is :",n)

c = t2.count(20)
print(c)

d = s1.index("radha")
print(d)

e = sum(t2)
print(e)

e = sum(t2,10) # sum 10 more to sum of all value in tuple
print(e)

      #---------- convert the tuple in list to change the tuple value , add ,remove

y = list(s1)
y[1] = 'lucy'
y.append("ravi")
y.remove('suman')
s1 = tuple(y)
print(s1)

      #------adding tuple to tuple

t2 += s1
print(t2)

print(tuple(t2 *2)) #multiply tuple

     #------unpacking tuple
s2 = ('suman', 'pintu', 'rohit', 20, 'dhrub', 'radha')
(green,*yellow,red) = s2
print(green, yellow ,red)
