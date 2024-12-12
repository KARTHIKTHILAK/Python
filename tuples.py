my_tuple = tuple(("Dave" , 42 , True))

another_tuple = (1,7,1,4,6,9)

print(my_tuple)
print(type(my_tuple))
print(type(another_tuple))

# adding a element in tuple is complex structure
new_list = list(my_tuple)
new_list.append("Neil")
new_tuple = tuple(new_list)
print(new_tuple)

# unpacking of tuple
(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)

print(" ")

print(another_tuple.count(1))