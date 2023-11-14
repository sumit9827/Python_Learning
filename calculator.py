num1 = float(input("Enter the First Numner : "))
num2 = float(input("Enter the Second Numner : "))

operator = input(" Enter the Operation you want to perform: ")

if operator == '+':
    print("Sum of the num1 and num2 :", num1 + num2)

elif operator == '-':
    print("Substraction of the num1 and num2 :", num1 - num2)

elif operator == '*':
    print("Multiplication of the num1 and num2 :", num1 * num2)

elif operator == '/':
    print("Division of the num1 and num2 :", num1 / num2)

else:
    print("Invalid Operator")





