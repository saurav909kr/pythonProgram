l= []
while True:
    c=int(input('''
    1.push Element
    2.pop first Element
    3.front Element
    4.Last Element
    5.Display Stack
    6.Exit
    '''))
    if c==1:
         n=input("Enter the value")
         l.append(n)
         print(l)
    elif c==2:
        if len(l)==0:
            print("Empty queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty queue")
        else:
            print("last stack value",l[0])
    elif c==4:
        print("Last queue element",l[-1])
    elif c==5:
        print("display queue element", l)
    elif c==6:
        break
    else:
        print('invalid choice')