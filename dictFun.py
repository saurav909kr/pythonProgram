from traceback import print_tb

dict1 = {
    "Buyer" : "aryan",
    "lang" : "python",
     "fees" : 4000,
     "duration" :"2 month"
}

n = dict1.get('lang')
print(n)

n = dict1.keys()
print(n)

for n in dict1.keys():
    print(n,end=", ")

print()

n = dict1.values()
print(n)

for n in dict1.values():
    print(n,end=", ")

print()

n = dict1.items()
print(n)

for n in dict1.items():
    print(n,end=", ")

print()

del dict1['lang']
print(dict1)

# n = dict1.pop('fees')
# print(n)

dict1.pop('fees')
print(dict1)

d = dict(name = 'saurabh',course = 'b.tech',branch='Data Science')
print(d,type(d))

dict1.update({"fees": 12000})
print(dict1)

# d.clear()
# print(d)

d['reg no'] = "240976383"
print(d)

d['name'] = 'abhijeet'
print(d)












