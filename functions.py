# Functions
def hello_world():
    print("Hello, World")

hello_world()

def sum(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2

total = sum(9,9)
print(total)

def sum(num1, num2=1):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2

total = sum(9)
print(total)

def sum(num1=1, num2=1):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2

total = sum()
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Karthik","Thilak","Sports")

def add(*num):
    sum = 0
    for n in num:
        sum = sum+n
    print("Sum : ",sum)

add(2,6,8999,933455,643937)

def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_named_items(first = "Share",last = "Like")

def func(a,b,*args,option = False,**kwargs):
    print(" ")
    print(a,b)
    print(args)
    print(option)
    print(kwargs)

func(1,3,10,20,Name = "Karthik",Salary = 10000000)


# Recursion

def add_one(num):
    
    if(num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total)

my_new = add_one(0)
print(my_new)



# Program to print factorial of a number 
# Recursively.

# Recursive function
def recursive_factorial(n):
    if n ==1:
        return n 
    else:
        return n * recursive_factorial(n-1)

# user input
num = int(input("num : "))

# check if the input is valid or not 
if num < 0 :
    print("Invalid input ! Please enter a positive number.")
elif num == 0 :
    print("Factorial of number 0 is 1")
else:
    print("Factorial of number",num,"=",recursive_factorial(num))