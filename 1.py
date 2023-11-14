# myDict={'Str1':'Sumit', 'identity':'Father'} 
# print(myDict['Str1'] + " has identity as " + myDict['identity'])
# myDict['Str1'] = "Shwetank"
# myDict['identity'] = 'son'
# print(myDict['Str1'] + " has identity as " + myDict['identity'])

count = 10
while(count > 0):
    print("*" * count)
    count -=1


for i in range(1,11):
    print("*" * i)

myList = ["Hey There", "one","two","......"]
for s in myList:
    print(s)

for i in range(1,11):
    if i == 8:
        break
        print("in IF" , i)
    print(i)

for i in range(1,11):
    if i == 8:
        continue
        print("in IF" , i)
    print(i)

for i in range(1,11):
    if i >=9:
        pass
        print("in IF" , i)
    print(i)
