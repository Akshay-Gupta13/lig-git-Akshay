num1 = float(input("Enter your first operand: "))
op = input("Enter operator: ")
num2 = float(input("Enter your second operand: "))

if op == "+":
    print(num1+num2 )
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)        
else:
    print("ghar pe bol calculator dilaye -_-")    