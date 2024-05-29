# Dictionary is a perfect way to represent any form of data, this include nesting

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
# performing a looping through the dictionary
for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

print(len(aliens))
print("\nfirst 5 aliens:")
for alien in aliens[:5]:

    print(alien)
print("...")

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

print("\nthe first set of 5 aliens:")

for alien in aliens[:5]:
    print(alien)

# storing lists in a dictionary

pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}

print(
    "\nYou ordered a "
    + pizza["crust"]
    + "-crust pizza "
    + "with the following toppings:"
)

for topping in pizza["toppings"]:
    print("\t" + topping)


favorite_languages = {
    "jen": ["python", "ruby"],
    "frank": ["python", "javascript"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(name.title() + "'s favorite language:")
    else:
        print(name.title() +"'s favorite language is:")
    for language in languages:
        print("\t"+ language.title())
