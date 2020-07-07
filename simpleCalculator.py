num1 = float(input("Enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Enter a number: "))

if op == "+": #python does not require equals() string comparison
    print(num1+num2)
elif op == "-":
    print(abs(num1-num2))
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")