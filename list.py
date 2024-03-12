# Lists

# fruits=["apple,banana,mango"]
# print(fruits)


# fruits=["apple","banana","mango","apple","banana","apple","banana","apple","banana"]
# print(fruits)

# for finding how many item present in the list we have to use len()

# fruits=["apple","banana","mango","apple","banana","apple","banana","apple","banana"]
# print(len(fruits))


# # Data type:- string, intm boolean
# list1 = ["apple", "banana", "cherry"]
# print(type(list1))

# list2 = [1, 5, 7, 9, 3]
# print(type(list2))


# list3 = [True, False, False]
# print(type(list3))

# # A list with strings, integers and boolean values:
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# Using the list() constructor to make a List:
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# Access ltem list
# thislist = ["apple", "banana", "cherry"]
# print(thislist[0])

# find range of the index
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[3:])

# thislist = [ "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else:
#   {
#     print("No it is not in the fruit list")


# Change item value

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)


# add list item using append()

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# add list item using insert()
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)


# add list item using Extend()
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# color=["black","green","blue"]
# tropical=["red","brown"]
# color.extend(tropical)
# print(color)

# remove item
# color=["black","green","blue"]
# color.remove("blue")
# print(color)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)



# Loop list

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# color = ["black","red"]
# for i in range(len(color)):
#   print(color[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# color = ["red","black","purple"]
# i=0
# while i< len(color):
#   print(color[i])
#   i = i+1


# list comprehension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # newlist = [x for x in fruits if "a" in x]
# # newlist = [x for x in fruits if x != "apple"]
# # newlist = [x for x in fruits]
# # newlist = [x for x in range(6)]
# # newlist = [x.upper() for x in fruits]
# # newlist = [x.lower() for x in fruits]
# # newlist = [x for x in range(10) if x < 5]
# # newlist = [x if x != "banana" else "orange" for x in fruits]
# # newlist = [x if x != "cherry" else "lichi" for x in fruits]

# print(newlist)



# Sort list

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# color = ["red","blue","black","green"]
# thelist = color.copy()
# print(thelist)

# color = ["red","blue","black","green"]
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# list3 = color + thislist
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# list methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()
