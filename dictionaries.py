car = {
    "brand": "Tesla",
    "model": "Model_3_P",
    "year": 2024
}

car2 = dict(
    brand="Tesla",
    model="Model_4",
)

print(car)
print(car2)
print(type(car))
print(len(car))

print(" ")

# access the items
print(car["brand"])
print(car.get("model"))

print(" ")

# list all keys
print(car.keys())

print(" ")

# list all value
print(car.values())

print(' ')

# list of key/value pairs as tuples
print(car.items())

print(" ")

# verify a key exists
print("model" in car)
print("price" in car)

print(" ")

# change value
car["brand"]="Nio"
car.update({"price":1000000})

print(" ")

print(car)

print(" ")

# remove items
print(car.pop("price"))
print(car)

print(" ")


car["EV"]="yes"
print(car)

print(" ")

print(car.popitem())
print(car)

print(" ")

# delete and clear

car["EV"] = "yes"
del car["EV"]
print(car)

car2.clear()
print(car2)

del car2

print(" ")

# coping dictionaries

car2 = car  # create a reference
print(" ")

# print("Bad Copy !")
# print(car2)
# print(car)

# car2["EV"] = "no"
# print(car)

car2 = car.copy()
car2["EV"] = "no"

print(" ")

print("Good Copy")
print(car)
print(car2)

    # or use the dict() constructor functions
car3 = dict(car)
print(" ")
print("Good Copy")
print(car3)

# Nested dictionaries

number1 = {
    "name": "page",
    "instrument": "brand"
}
number2 = {
    "name": "page",
    "instrument": "model"
}
band = {
    "member1": number1,
    "member2": number2
}

print(" ")
print(band)

print(band["member1"]["name"])
print(band["member2"]["instrument"])