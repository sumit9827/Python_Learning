# class Student:
#     name = ''
#     score = 0
#     email ='temp@temp.com'

# print(type(Student))
# object_1 = Student()
# print(type(object_1))

# print(isinstance(object_1, Student))

# object_2 = Student()

# object_1.name = "sumit"
# object_1.email = "sumit@vcb.cvb"
# object_2.name

# print(object_1.name, object_1.email)
# print(object_2.email)


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.email = name + "@xyz.com"
#     # name = "Sumit"
#     # email = name + "@xyz.com"

# s1 = Student("sumit")
# print(s1.name, s1.email)

# s2 = Student("matt")
# print(s2.name, s2.email)


# class Student:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + "." + last + "@xyz.com"
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def UpperCase(self):
#         self.first = self.first.upper()
#         self.last = self.last.upper()

# s1 = Student("sumit", "Srivastava")
# s2 = Student("Shubhang", "Srivastava")

# s = Student.fullname(s2)
# print(s)
# print(s1.fullname(), s1.email)

# print(Student.fullname(s1))
# del s1
# del s1.first
# print(s1.last)
# print(s1.first)

# s1.UpperCase()
# s2.UpperCase()


# print(Student.fullname(s1))
# s = Student.fullname(s2)
# print(s)

class Competition:
    raise_amount = 1.04
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def raise_prize(self):
        self.prize = self.prize * Competition.raise_amount
    

debate = Competition("Debate", 700)

print(debate.name, debate.prize)

print(Competition.raise_amount)

debate.raise_prize()

print(debate.prize)


 