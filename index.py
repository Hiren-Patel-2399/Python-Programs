# # print("Hello, world")


# # if 5 > 2:
# #   print("Five is greater than two!")

# # if 5 > 2:
# #  print("Five is greater than two!") 
# # if 5 > 2:
# #         print("Five is greater than two!") 

# # if 5 > 2:
# #  print("Five is greater than two!")
# # if     5 >       2:
# #         print("Five    is greater    than two!")


# # ----------------------------------------------------------------------
# # ----------------------------------------------------------------------
# # ----------------------------------------------------------------------

# # variables 

# # legal variable name:--
# # myvar = "John"
# # my_var = "John"
# # _my_var = "John"
# # myVar = "John"
# # MYVAR = "John"
# # myvar2 = "John"



# # Camel case:-- myVariableName = "John"

# #Pascel case:-- MyVariableName = "John"

# #Snake case:-- my_variable_name = "John"

# # x=34
# # x="hiren"
# # print(x)


# # x=50
# # y=60
# # z = (x+y)
# # print (z)

# # x=503
# # y=23
# # z=x%y
# # print(z)

# # x=233
# # y=123
# # z=4367

# # a=(x+y)%z

# # print(a)

# # for same value of differnt variable
# # x =y =z ="Orange"


# # Assign multiple values
# # x, y, z = "Orange", "Banana", "Cherry"
# # print(x)
# # print(y)
# # print(z)


# # unpack
# # fruits = ["apple", "banana", "cherry"]
# # x, y, z = fruits
# # print(x)
# # print(y)
# # print(z)


# # Output varables
# # x = "Python is awesome"
# # print(x)

# # Global variable
# # x = "awesome"

# # def myfunc():
# #   x = "fantastic"
# #   print("Python is " + x)

# # myfunc()

# # print("Python is " + x)

# # def myfunc():
# #   global x
# #   x = "fantastic"

# # myfunc()

# # print("Python is " + x)

# # x = "awesome"

# # def myfunc():
# #   global x
# #   x = "fantastic"

# # myfunc()

# # print("Python is " + x)

# # x= str(3)
# # y= int(5)
# # z= float(45)

# # print(x,y,z)

# # x = 5
# # y = "John"
# # print(type(x))
# # print(type(y))

# # a = 4
# # a = "Sally"
# # print(a,a)


# # --------------------------------------------------------------------
# # --------------------------------------------------------------------
# # --------------------------------------------------------------------

# # Python data type

# # 1 builtin data type

# # Text Type:	str
# # Numeric Types:	int, float, complex
# # Sequence Types:	list, tuple, range
# # Mapping Type:	dict
# # Set Types:	set, frozenset
# # Boolean Type:	bool
# # Binary Types:	bytes, bytearray, memoryview
# # None Type:	NoneType

# # x = 5
# # print(type(x))

# # list denoted by square braket[]
# # x = ["apple", "banana", "cherry"]

# #  tupel denoted by circle braket()
# # x = ("apple", "banana", "cherry")

# # dict denoted by curly braket and colon{:}
# # x = {"name" : "John", "age" : 36}

# # set denoted by curly braket and comma{,}
# # x = {"apple", "banana", "cherry"}

# # frozenset denoted by curly and circle({})
# # x = frozenset({"apple", "banana", "cherry"})

# # boolean
# # x = True

# # bytes
# # x = b"Hello"


# # bytearray 
# # x = bytearray(5)
# # print(x)

# # memory view
# # x = memoryview(bytes(5))
# # print(x)




# # --------------------------------------------------------------------
# # --------------------------------------------------------------------
# # --------------------------------------------------------------------

# # Python Number

# # x = 1    # int
# # y = 2.8  # float
# # z = 1j   # complex

# # #convert from int to float:
# # a = float(x)

# # #convert from float to int:
# # b = int(y)

# # #convert from int to complex:
# # c = complex(x)

# # print(a)
# # print(b)
# # print(c)

# # print(type(a))
# # print(type(b))
# # print(type(c))



# # import random

# # print(random.randrange(1, 10))


# # x=5
# # x= float(x)
# # print(x)

# # x=10
# # x= complex(x)
# # print(x)

# # x=12.573
# # x=int(x)
# # print(x)


# # String
# # a = '''Lorem ipsum dolor sit amet,
# # consectetur adipiscing elit,
# # sed do eiusmod tempor incididunt
# # ut labore et dolore magna aliqua.'''
# # print(a)



# # a="hello world!"
# # print(a[4])

# # ?find length 
# # a = "Hello, World!"
# # print(len(a))

# # check strimg
# # txt = "The best things in life are free!"
# # print("free" in txt)

# # txt = "The best things in life are free!"
# # if "free" in txt:
# #   print("Yes, 'free' is present.")

# # txt = "The best things in life are free!"
# # if "expensive" not in txt:
# #   print("No, 'expensive' is NOT present.")



# # b = "Hello, World!"
# # print(b[:5])

# # b = "Hello, World!"
# # print(b[-5:-2])



# # modify string
# # upper case
# # a = "Hello, World!"
# # print(a.upper())

# # lower case

# # a = "Hello, World!"
# # print(a.lower())

# # strip case 
# # a = " Hello, World! "
# # print(a.strip())


# # Replace case
# # a = "Hello, World!"
# # print(a.replace("H", "J"))

# # Split case
# # a = "Hello, World!"
# # print(a.split(",")) 





# # string concentation
# # a = "Hello"
# # b = "World"
# # c = a + b
# # print(c)


# # a = "Hello"
# # b = "World"
# # c = a + " " + b
# # print(c)

# # string format 
# # age = 36
# # txt = "My name is John, and I am {}"
# # print(txt.format(age))


# # age = 40
# # txt = "My uncle age {}"
# # print(txt.format(age))



# # The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

# # quantity = 3
# # itemno = 567
# # price = 49.95
# # myorder = "I want {} pieces of item {} for {} dollars."
# # print(myorder.format(quantity, itemno, price))

# # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

# # quantity = 3
# # itemno = 567
# # price = 49.95
# # myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# # print(myorder.format(quantity, itemno, price))


# # Escape
# # txt = "We are the so-called \"Vikings\" from the north."
# # print(txt)


# # Boolean Value 
# # print(10 > 9)
# # print(10 == 9)
# # print(10 < 9)


# # a = 20
# # b = 33

# # if b > a:
# #   print("b is greater than a")
# # else:
# #   print("b is not greater than a")


# # x = "Hello"
# # y = 15

# # print(bool(x))
# # print(bool(y))

# # class myclass():
# #   def __len__(self):
# #     return 0

# # myobj = myclass()
# # print(bool(myobj))


# # def myFunction() :
# #   return True

# # print(myFunction())

# # def myFunction() :
# #   return True

# # if myFunction():
# #   print("YES!")
# # else:
# #   print("NO!")


# # Python Operator

# # Arithmetic operators
# # Assignment operators
# # Comparison operators
# # Logical operators
# # Identity operators
# # Membership operators
# # Bitwise operators

# # operator precedence
 
# # print((6+3)-(10+3))

# # print(100+3*4)



# # Lists

# fruits=["apple,banana,mango"]
# print(fruits)


