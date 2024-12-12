grocery_list = ["Apple","Milk","Egg"]

data = ["Karthik" , "18" , True]

empty_list = []

print("Apple" in grocery_list)

print(" ")

print(data[0])
print(data[-1])
print(grocery_list.index("Milk"))
print(grocery_list[0:2])
print(grocery_list[0:])
print(grocery_list[-3:-1])

print(" ")

# length
print(len(grocery_list))
print(len(data))

print(" ")

# append
grocery_list.append("Orange")
print(grocery_list)

print(" ")

# normal
grocery_list += ["Rice"]
print(grocery_list)

print(" ")

# extend
grocery_list.extend(["Fish" , "Chicken"])
print(grocery_list)

print(" ")

grocery_list.extend(data)
print(grocery_list)

print(" ")

# insert
grocery_list.insert(0,"Mutton")
print(grocery_list)

print(" ")

grocery_list[2:2] = ["Pepper","Onion"]
print(grocery_list)

print("")

grocery_list[1:3] = ["Chilli","Tomato"]
print(grocery_list)

print(" ")

# remove
grocery_list.remove("18")
print(grocery_list)
grocery_list.remove(True)
print(grocery_list)

print(" ")

# pop
print(grocery_list.pop())
print(grocery_list)

print(" ")

# del
del grocery_list[0]
print(grocery_list)

# del data
# print(data)

print(" ")

# clear
data.clear()
print(data)

print(" ")

# sort
grocery_list.sort()
print(grocery_list)

print(" ")

grocery_list[1:2] = ["Salt"]
grocery_list.sort()
print(grocery_list)

print(" ")

grocery_list.sort(key=str.lower)
print(grocery_list)

print(" ")

# NUMBER in LIST
number = [1 , 5 , 7 , 3 , 9]
number.reverse()
print(number)

print(" ")

number.sort()
print(number)               # ascending

print(" ")

number.sort(reverse=True)
print(number)               # descending

print(" ")

# sorted for globally
number = [22,33,45,42,78,99,45]
print(sorted(number, reverse=True))
print(number)

print(" ")

# Copying of LIST
number_copy = number.copy()
my_number = list(number)
my_copy = number[:]

print(" ")

print(number_copy)
print(my_number)
my_copy.sort()
print(my_copy)

print(" ")
print(number)
print(type(number))

print(" ")

# constructor function

my_list = list(["Karthik" , "Thilak"])
print(my_list)