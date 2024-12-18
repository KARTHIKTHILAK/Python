# lambda 
squared = lambda num : num * num
print(squared(3))


add_two = lambda num : num + 2
print(add_two(8))
# def add_two(num) : return num + 2

sum_total = lambda a, b : a + b
print(sum_total(8,9))
# def um_total(8,9) : return a+b
print(' ')



def funBuilder(x) :
    return lambda num : num + x

add_ten = funBuilder(10)
add_twenty = funBuilder(20)

print(add_ten(7))
print(add_twenty(7))


numbers = [1,2,3,12,39,56]

squared_nums = map(lambda num : num * num , numbers)

print(list(squared_nums))


odd_nums = filter(lambda num : num % 2 != 0 ,numbers)

print(list(odd_nums))

from functools import reduce 

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr : acc + curr , numbers)

print(total)

print(sum(numbers))

names = ['Karthik' , 'Thilak' , "Kumar" , "Kalaivani"]

char_count = reduce(lambda acc , curr : acc + len(curr) , names , 0)

print(char_count)
