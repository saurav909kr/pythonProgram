st = {
    'Manisha':{'course':"data science", 'reg no':873289509},
    'vijay': {'course': "chemical science", 'reg no': 87346509},
    'rajiv': {'course': "EEE", 'reg no': 87368509},
    'monika': {'course': "computer science", 'reg no': 875559509}
}

print(st)
print(st['vijay'])

print(st['monika']['reg no'])

for k,v in st.items():
    print(k,v['course'],v['reg no'])

for k,v in st.items():
    print(k)
    for x in v :
        print(x+':',v[x])


st['monika']['course'] = 'chemical'
print(st)

del st['monika']['course']
print(st)

x = st.copy()
print(x)

n = st['Manisha'].get('course')
print(n)

n = st['Manisha'].keys()
print(n)

n = st['Manisha'].values()
print(n)

st['rajiv'].popitem()
print(st)

x=st['rajiv'].setdefault('course','computer science')
print(x)

st['vijay']['course'] = 'mech'
print(st)

st['vijay']['hobbies'] = "reading"
print(st)

st['himanshu'] = {'course':'data science','hobbies':'football'}
print(st)