dict1 = {
    "lang" : "python",
     "fees" : 4000,
     "duration" :" 2 month"
}

print(dict1,type(dict1),'\n')

print(dict1["lang"],'\n')

for a in dict1:
    print(a,":",dict1[a],end=", ")