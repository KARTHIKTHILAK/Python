nums = {1,2,3,4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed

nums3 = {1,2,2,3,4}
print(nums3)

# True is a dupe of 1, False is a dupe of zero
nums4 = {1,True,2,False,3,4,5}
print(nums4)

# check if a value in set
print(2 in nums4)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to a set
nums4.add(8)
print(nums4)

# add element from one set to another 
more_nums = {5,6,7}
nums4.update(more_nums)
print(nums4)

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set
one = {1,2,3}
two = {4,5,6}

my_new_set = one.union(two)
print(my_new_set)

# keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)