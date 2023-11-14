import getpass

user_name = input("Enter your user name :  ")
user_password= getpass.getpass("Enter your password :  ")

print("the username is {}\n user password is {}".format(user_name, user_password))