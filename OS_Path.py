# Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> import os.path
# >>> if os.path.exists('C:\sumit\Python_Learning'):
# ...     print("Path Exists")
# ... else:

# city = 'Los Angles'
# words = "this is my life and i dont know why i am spiling my life".split()
# print(words)
# l = [len(word) for word in words]
# print(l) 

# from math import factorial

# f = [str(factorial(x)) for x in range(5)]
# print(f)

# country_to_capital= { 'UK' : 'london', 'brazil' : 'Brasilia',
#                         'india' : 'New Delhi',
#                         'USA' : 'Washington', 'Pakistan' : 'islamabad'}

# # print(capital_to_country)
# capital_to_country = {capital: country for country , capital in country_to_capital.items()}

# from pprint import pprint as pp
# pp(capital_to_country)
# from math import sqrt

# def is_prime(x):
#     if x <2:
#         return False
#     for i in range(2, int(sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True

# sf = [x for x in range(101) if is_prime(x)]
# print(sf)

# num = 20

# print("Num before expression", num)

# num = num -20 if num > 30 else num + 10

# print("Num after expression", num)


# age = 67

# name = "Sumit Kumar Srivastava"

# intro = "My name is {} and My Age is {}"

# print(intro.format(name, age))
# numList = '1 2 3 4 5 6 7 8 9'
# s = numList.split()

# print(s)

# name = ['Sumit','Kumar','Srivastava']

# joined_name = '_'.join(name)

# print(joined_name)

text1 = "This is old text"

text2 = text1.replace('old', 'new')
print(text2)