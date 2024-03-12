# class Student:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# x = Student("Deep", "Heer")
# x.printname()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# x = Student("Neel", "Mansi")
# x.printname()


# class name:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Person(name):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationaryear = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationaryear)


# x = Person("Hiren", "Patel", 2022)
# x.welcome()

# x = Person("Hiren", "Patel")
# print(x.graduationaryear)


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


