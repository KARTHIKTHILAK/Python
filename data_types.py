# String Data Type

    # literal assignment
first_name = "Karthik"
second_name = "Thilak"

print(type(first_name))
print(type(second_name)  == str)
print(type(first_name) == int)
print(isinstance(first_name, str))


    # constructor function
father = str("Kumar")
mother = str("Kalaivani")
print(type(father))
print(type(father) == int)
print(isinstance(father, str))

# Concatenation
full_name = first_name + " " + second_name
print(full_name)



# Casting a number to string
decade = str(2024)
print(type(decade))
print(decade)

statement = "I like Programming and Sports" + " " + decade + "s."
print(statement)

multi_line = """
Hi Welcome to Python programming
    I learn in the Youtube
        I like This
"""
print(multi_line)


sentence = 'I\'m Karthik \t Welcome \n Enter in the new line'
print(sentence)

print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.replace("Welcome","Subscribe"))

print(len(sentence))

sentence+="                       "
sentence = "         " + sentence
print(len(sentence))

print(len(sentence.strip()))
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))



# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".")+"$1".rjust(4))
print("Muffin".ljust(16, ".")+"$2".rjust(4))
print("Cheesecake".ljust(16, ".")+"$4".rjust(4))

print("")


# string Index Value
first = "Subscribe"
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("S"))
print(first.endswith("b"))


# Boolean Data Type

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))


# Numerical Data Type

    # Integer Type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))

    # Float Type
gpa = 9.99
y = float(9.56)
print(type(gpa))
print(isinstance(y,float))

    # Complex Type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Build-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa,1))

import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to Number 
zipcode = "636307"
zip_value = int(zipcode)
print(zip_value)

# Error if you attempt to cast incorrect data
zip_value_2 = int("New York")