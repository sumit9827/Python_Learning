# # def nameOfFunction(param):
# #     your code
# #     return

def addition(num1, num2):
    return num1 + num2


def division(num1, num2):
    if num2 == 0:
        return "ERROR: can not divide by zero"
    else:
        return num1/num2

var1 = 12 
var2 = 0

result = addition(var1, var2)
print("Result of addition: ", result)

result = division(var1, var2)
print("Result of division: ", result)

