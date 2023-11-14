str_val = input("Enter the String Value")

reversed_str = str_val[::-1]

if str_val == reversed_str:
    print("String is palindrome")
else:
    print("String is not palindrome")