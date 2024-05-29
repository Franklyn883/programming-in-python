alien_0 = {"color": "green", "point": 5}

print(alien_0["color"])
print(alien_0["point"])

# adding value to a dictionary

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print("alien_0:", alien_0)

alien_1 = {}
alien_1["color"] = "red"
alien_1["point"] = 10
alien_1["x_position"] = 5
alien_1["y_position"] = 30

alien_0["speed"] = "medium"
print("alien_1:", alien_1)

print("Original x-position: " + str(alien_0["x_position"]))

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "fast":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

# We can use the "del" keyword to delete anything we want from the dictionary.

del alien_0["point"]
print(alien_0)
