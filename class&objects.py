# create class

# class myclass:
#     x = 5 * 6

# p1 = myclass()
# print(p1.x)

 
# class person:
#     def __init__(self, name , age, hobby):
#         self.name = name 
#         self.age = age
#         self.hobby = hobby

# p1 = person("Hiren", 45, "Criket")

# print(p1.name)
# print(p1.age)
# print(p1.hobby)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = Person("Hiren", 45)

# print(p1)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is" + self.name)

# p1 = Person("Hiren", 23)

# p1.age = 13

# print(p1.age)

# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# x = person("Hiren","Patel")
# x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     pass

# x = Student("Deep", "Heer")
# x.printname()

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()

