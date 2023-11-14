#import getpass
#user_password = ""

#while user_password != "Ron$123":
 #   user_password = getpass.getpass("Enter your password :  ")

#print("\n Access Granted") 

# user_name = input("Enter the name: ")
# user_input = int(input("Enter the Value: "))

# Count = 0

# while Count <= user_input:
#     print(Count, ":", user_name)
#     Count = Count + 1

# num = 0

# while num in range(0, 10):
#     print(num)

#     num = num + 1

# num = 0

# while num in range(0, 26):
#     if num % 2 == 0:
#         print("Number", num , "is a even number")
#     else:
# #         print("Number", num , "is odd number")
    
# #     num = num +1

# x, y = 0, 8
# while(x < y): x =x +1; print(x)

# x = 1

# while x <= 5:
#     y = 1
#     while y <= 5:
#         print(x,y)
#         y = y +1
#     print(x, y)
#     x = x+1

# my_list = [10,20,30,40,50,60]

# count = 0
# total = 0
# while count < len(my_list):
#     print(my_list[count])
#     count +=1
#     total +=my_list[count-1]

# print("there are %d element are there in list" % count)
# print("Sum of all element is %d" % total)

# num_list = range(0, 50)
# print(num_list)

# even_list = []
# odd_list = []
# i = 0
# while i < 50 :
#     # print(i)
#     if i % 2 == 0:
#         even_list.append(i)

#     else:
#         odd_list.append(i)
    
#     i += 1

# print(even_list)

# print(odd_list)

# temperature = [-47, -56, -54, -26, -3, 4, 6, 20,  67, 89, 10, 23]
# print('    C    F')
# index = 0
# while index < len(temperature):
#     C = temperature[index]
#     F = (9.0/5)*C + 32
#     print("%5d %5.1f" %(C, F))
#     index +=1

# character_name = ['sumittttttttttttttttttttt', 'kumaraaaaaaaaa', 'Srivastava']

# long_name = character_name[0]

# index = 0

# while index < len(character_name):
#     if len(long_name) < len(character_name[index]):
#         long_name = character_name[index]
#     index =index + 1

# print("the longest name in list is %s" %long_name)

# num = 20

# while num < 50:
#     print(num)
#     if num == 40:
#         break
#     num += 5

# num = 10

# while True:
#     num = int(input("Enter the number: "))
#     if num % 3 == 0:
#         break
# print("\n We are out of loop")

# place = "NewYorkCity"

# index = 0

# place_length = len(place)

# while index in range(place_length):
#     if place[index] == "i":
#         break
#     print(place[index])
# #     index = index +1

# clean_haystack = ['hay','hay','hay','hay','hay','hay','hay','hay','hay','hay','hay','hay']
# unclean_haystack = ['hay','hay','hay','hay','hay','hay','needle','hay','hay','hay','hay','hay','hay']

# index = 0

# searching_for = 'needle'

# max_len_haystack = len(unclean_haystack)

# while index < max_len_haystack:
#     if searching_for == unclean_haystack[index]:
#         print("Needle found at index at %s" %index)
#         break
#     index = index +1
# else:
#     print("Needle not found")

# num = range(0, 10)
# i = 0
# while i in num:
#     print(i)
#     if i == 5:
#         pass
#         print("This is pass")
#     i = i + 1

# num = 0
# while num < 100:
#     num = num +1
#     if num % 2 == 0 :
#         continue 
#     print("Odd Number : ", num)

# my_list = []
# num = 0

# while num in range(0, 50):
#     num = num + 1
#     if num % 5 == 0 or num % 7 == 0:
#         continue
#     my_list.append(num)

# print(my_list)

# while True:
#     val = input("Enter the Value: ")

#     if val == "out":
#         print("Exiting . Good Bye. Break statement executed")
#         break

#     if val.isdigit() == False:
#         print("Enter Integer only")
#         continue

#     val = int(val)
#     print("Cube of number %d is %d" %(val, val ** 3) )

x = 4
while x < 4+6:
    print(x)
    x += 1