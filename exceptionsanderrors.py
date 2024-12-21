
x= 2

try:
    print(x/0)

except NameError :
    print("Name is coming for user")

except ZeroDivisionError :
    print("Give a correct number")

except Exception as error:
    print(error)

else :
    print("No error")

finally : 
    print("Its is final for all")