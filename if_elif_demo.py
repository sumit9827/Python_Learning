grade = int(input("Enter the Grade you received:  "))

if 45 <= grade < 60:
    print("you are second grade student")

elif 60 < grade < 75:
    print("you are 1st class student")
elif grade > 75:
    print("you got distinction")
else:
    print("you are faile.!! do more hard work")
