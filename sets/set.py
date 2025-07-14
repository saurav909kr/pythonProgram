s = { False, 78, "hellow", 8.8, True, 0, 78 , 1} #true and 1 treated as duplicate , false and 0 treated as duplicate
print(s)
print(type(s))
print(len(s)) # duplicate treated as 1 in length

l = [55,89,'love', 9.9, 0.3]
print(set(l),type(set(l)))

#------set construction

s1 = set(('hel', 55, True, 'boka', 78))
print(s1)



for a in s1: #-------access set item
    print(a)

print()
print('hellow' in s1)
print( 90 in s1)


s1.add(False)
print(s1)

l = [87 , 55, 90, "rahul", 9.9, 0]
s1.update(l)
print(s1)

print()
s1.remove(False) #if item is not present raise an error
s1.remove("boka")
s1.discard(55)
s1.pop() #delet any value
print(s1)

print()
# s1.clear()      #delet all value and return set()
# print(s1)
# del s1          # delete set permanent

s2 = { 22,40,55,6,77,'rupam'}
s3 = {'light', 89, "hi", True}
s5 = { 'suman', 'budhu', 'mangun'}

s4 = s2.union(s3 ,s5)  # also union like this --> s4 = s2|s3|s5
print(s4)

print()
s6 = {22,40,56,88,99}
s7 = { 40,99,49,100,44}
set_ = { 22,40,99}

s8 = s6.intersection(s7) # alo use This(&) for intersection
s9 = s6.difference(s7)
print("same :",s8, "difference :" , s9)

print(s6.isdisjoint(s7))

print(set_.issubset(s6))

