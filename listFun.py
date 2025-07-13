l = [10, 45, 67 , 64, 10, 56]
p = ['hello', 'world']

a = l.count(10)
print(a)

m = max(l)
print(m)

n = max(p)
print(n)

l.sort()
print(l,'\n')

l.reverse()
print(l,'\n')

list1 = [10,20,30,40]
list2 = [55,56,78,99,100]

for a,b in zip(list1,list2):
    print(a,b,'\n')

               #-------convert the string into list

n = input("Enter the string")
print(n,'\n')
l = n.split()
print(l,'\n')

              #------take multiple input and get it in list

li = []
for a in range(1,4):
    n = input("Enter the value"+str(a)+":-")
    li.append(n)

print(li)


