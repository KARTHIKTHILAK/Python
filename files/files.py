import os
# r = Read
# a = Append
# w = Write
# x = Create
# 


# Read - error if it doesn't exists

f = open("files/names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f :
    print(line)

# Close

f.close()

try :
    f = open("files/names.txt")
    print(f.read())
except :
    print("The file does exists")
finally :
    f.close()


# Append - creates the file iƒ it doesn't exists
f = open("files/names.txt" , "a")
f.write("Selvaraj")
f.close()

# Write (Overwrite)
f = open("files/content.txt" , "w")
f.write("I deleted all of the content")
f.close()

f = open("files/content.txt")
print(f.read())
f.close()

# Create

# Two ways to create a new file 

# Open a file for writing, creates the file if it does not exists
f = open("files/name_list.txt" , "w")
f.close()

# Create the specified file , but returns an error if the file exists
if not os.path.exists("files/additional_names.txt") :
    f = open("files/additional_names.txt" , "x")
    f.close()



# Delete a file 

# avoid an error if it doesn't exists
if os.path.exists("files/additional_names.txt") :
    os.remove("files/additional_names.txt")
else :
    print("The file doesn't exists")


# with has build-in implicit exception handling
# close() will be automatically called

with open("files/more_names.txt") as f :
    content = f.read()

with open("files/name_list.txt" , "w") as f :
    f.write(content)