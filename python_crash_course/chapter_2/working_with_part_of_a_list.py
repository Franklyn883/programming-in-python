# we can work with a subset of a list, we simply choose the aspect of the list we want to work with
# using sliced
players = ["charles","lucky","great","jude","emeka","james"]
sliced_players = players[:2]
print(sliced_players)
print(players[2:])
print(players[-5:])
print(len(players))

# we can copy an entire list by using the slice operator

my_food = ["sliced bread", "fried rice", "banga rice", "beans"]
friend_food = my_food[:]
my_food.append("pizza")
print(my_food)
print(friend_food)

# The difference btw using a friend_food = my_food, if you make changes in one list, it affects the other because the both point to the same list
friend_food = my_food
friend_food.append("ice cream")
my_food.append("fried plantain")
print("here is my friends favorite food:\n")
print(friend_food)
print("\nhere is my favorite food:")
print(my_food)

print("\n The first three items in my food list are:")
print(my_food[:3])

print("\n three items from the middle of the list are: ")
print(my_food[2:5])

print("\n the last three items in the list are:")
print(my_food[-3:])
print("\nMy favorite food are:")
for food in my_food:
    print(food)