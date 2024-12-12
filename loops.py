# Loops

# While loop
i = 1
while i < 10:
    i = i+2
    if i == 3:
        continue
    print(i)
else:
    print("i is no longer less than 10")


# For loop
fruits = ["Apple","Banana","Mango"]
for i in fruits:
    print(i)

for banana in fruits:
    print("Karthik")

for i in "Share":
    print(i)

for i in "Share":
    print("Thilak")

for x in fruits:
    if x == "Banana":
        break
    print(x)

for x in fruits:
    if x == "Banana":
        continue
    print(x)


for i in range(10):
    print(i)

print(" ")

for i in range(2,4):
    print(i)

print(" ")

for i in range(0,101,5):
    print(i)
else:
    print("Glad that\'s over!")
    
# Nested loop
names = ["Karthik","Thilak","Kumar","Kalaivani"]
actions = ["codes","eats","works","house"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

print(" ")

for action in actions:
    for name in names:
        print(name + " " + action + ".")