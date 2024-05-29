car = "tesla"
print("is a car == 'tesla'? I predict True")
print(car == "tesla")
car = "toyota"
print("\nis car == 'toyota'? I predict True")
print(car == "toyota")
print("\ncar == 'honda'? I predict False")
print(car == "honda")

age_0 = 16
age_1 = 18

if (age_0 >= 18) and (age_1 >= 18):
    print("welcome to the club")
else:
    print("Sorry!, you both need to be 18 to enter")

if (age_0 >= 18) or (age_1 >= 18):
    print("welcome to the club!")

else:
    print("sorry!, one of you need to be 18 to enter")

cars = ["benz", "jaguar", "toyota", "jeep"]
print("\n")
if "honda" in car:
    print("I have a honda!")
else:
    print("we don't have honda at the moment!")

if "honda" not in car:
    print("\nnot in stock")
else:
    print("we have in stock")

# the if-elif-else chain: for two possible outcome, using
# if and else is okay, but for more possible outcome
# we can use a chain of if-elif-else block.
print("\n------------------if-elif-else chain -------------------\n")
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif (age < 65):
    price = 10
elif (age >= 65):
    price = 5

print("Your admission price is $"+str(price)+".")

# using chained if-elif-else is great for testing conditions
# where you want one condition to pass the test.
# but when more than one condition can be true, it's better to just use
# a chained if statements.
print("\n")
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza")

# if you want only one block of code to run, use an if-elif-else chain.
# if more than one block of code needs to run, use a series of independent if
# statements.

print("\n --------------------Exercise-------------------\n")

alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points.")

alien_color = "red"

if alien_color == "green":
    print("you earned 5 points for shooting the alien.")
elif alien_color == "yellow":
    print("you earned 10 points for shooting the alien.")
elif alien_color == "red":
    print("you earned 15 points for shooting the alien")

age = 65

if age < 2:
    print("you are a baby.")
elif age < 4:
    print("you are a toddler.")
elif age < 13:
    print("you are a kid.")
elif age < 20:
    print("you are a teenager.")
elif age < 65:
    print("you are an adult.")
elif age >= 65:
    print("you are an elder.")
