
num1 = int(input("enter the value"))
num2 = int(input("enter the value"))
opr = input("enter the oper..(+,-,*,/)")

if opr=="+":
    print(num1 + num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operator")


if opr=="+":
    print(num1 + num2)
if opr=="-":
    print(num1-num2)
if opr=="*":
    print(num1*num2)
if opr=="/":
    print(num1/num2)
if opr !="+" and opr !="-" and opr != "*" and opr != "/":
    print("invalid operator")