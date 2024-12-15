# Scope

name = "Karthik"
age = 15
def another():
    print(" ")
    global age  
    age = age + 1
    color = "green"
    def greeting(name):
        print(name)
        print(age)
        nonlocal color 
        color = "red"
        print(color)
    greeting("Share")

another()


# Closure is a function having access to the scope of its parent function after the parent function has returned.

def parent_function(person, coins):
    # coins = 3


    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1 :
            print("\n" + person + " " + "has " + str(coins) + " " + "coins left.")
        elif coins == 1 :
            print("\n" + person + " " + "has " + str(coins) + " " + "coin left.")
        else:
            print("\n" + person + " " + "is out of coins")

    return play_game

tommy = parent_function("Tommy", 3)
jenny= parent_function("Jenny", 5)

tommy()
tommy()

jenny()
jenny()

print(" ")

def make_multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

print(times3(9))

print(times5(3))

print(times5(times3(2)))
