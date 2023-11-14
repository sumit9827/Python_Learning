char = input("Please enter the character: ")
char = char.lower()

if char in ('a','e','i','o','u'):
    print(f"Entered Character {char} is vowel")
elif char == 'y':
    print("y is ambiguous. Depends upon where it got used")
else:
    print(f"Entered Character {char} is Consonent")
