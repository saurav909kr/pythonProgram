import json

#----converting the python object to json

dict1 = {
    'name':"saurabh",
    'course':'b.tech',
    'course duration':'4 year'
}
a = json.dumps(dict1)
print(a,type(a))
print()

#------converting the json to python object and reading

with open('data.json','r') as file:
    data = json.load(file)
print(data)
print(type(data))
for student in data['students']:
    print('id:',student['id'])
    print('name:',student['name'])
