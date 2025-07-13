
list_1 = [1,24,33 ,66]
print(list_1[2],type(list_1[2]))

list_2 = [2,98,90,"hello",[33, 55 ,99 ,0]]
print(list_2[3],"\n")

k =list_2[2:4]
print(k,type(k),'\n')

print(list_2[0::2],'\n')
print(list_2[-1::-1],'\n')

for a in list_2:
    print(a)

print('\n')

t = len(list_2)
for a in range(t-1, -1 , -1):
    print(list_2[a],end=", ")

print('\n')

del list_1[1]
print(list_1,'\n')

#print(list_2.pop(3))
#print(list_2,'\n')

list_1.remove(66)
print(list_1,"\n")

list_2[4] = "buddy"
print(list_2,'\n')

list_1.insert(0,"Good morning")
print(list_1,'\n')

list_1.append("love")
print(list_1,'\n')

list_1.extend(list_2)
print(list_1,'\n')

list_2.clear()
print(list_2)

