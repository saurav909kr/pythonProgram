      #-------Number datatype(--immutable--)

a = 5
print(a, type(a))

b = 4.4
print(b,type(b))

c = 4 + 5j
print(c,type(c))


      #-------string(--immutable--)[sequence dataType]

s = "hello9090"
print(s, type(s))

s = ''' 
   hello john sina 
       welcome to my hood
'''
print(s,type(s))

a = "10"
print(a,type(a))


    #------list(--mutable--)[sequence dataType]

l = [10,'ws',5.8, (3+4j)]
print(l,type(l))
l[2] = 10  # here i change the list at index 2
print(l,type(l))


    #-----Tuple(--immutable--)[sequence dataType]

t = (5, "mohan", 4.4) # in tuple there must be more than 1 value
print(t,type(t))
t = (5, "mohan", 4.4)
#t[1] = 30 ---> # it give error because it does not allow upgradation
print(t,type(t))
t = (5)
print(t,type(t))


   #----- dictionary dataType

d = {
    'name' : 'Saurabh kumar',
    'course': 'B.tech',
    'Branch' : 'Data Science'
}
print(d['Branch'])
print(d,type(d))

d['course'] = "MBA"
print(d,type(d))

d['city'] = "bhagalpur"
print(d,type(d))

del d['city']
print(d,type(d))

key_list = list(d.keys())
print(key_list, type(key_list))

item_list = list(d.items())
print(item_list, type(item_list))

str_1 = str(d)
print(str_1, type(str_1))


     #-----set dataTYpe

my_set = { 1, 2 , 1, 4}
print(my_set,type(my_set))

my_set2 = { 'saurabh', 2 , 3.4}
print(my_set2,type(my_set2))

my_set2.add(4.4)
my_set2.remove(3.4)
print(my_set2)

my_set2.update(["ram ji"])
print(my_set2)

my_set2.clear()
print(my_set2)

