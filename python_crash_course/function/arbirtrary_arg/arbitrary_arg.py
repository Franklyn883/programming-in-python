# Sometimes we may not know how many arguments will bee passed to our functions.
# to handle that we use arbitrary arguments.


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza("peperoni", "fresh sauce", "german tops")

# now let's use a for loop to nicely print everything in the tuple.


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following toppings:"
    )
    for topping in toppings:
        print("\t- " + topping)


make_pizza(12, "peperoni", "hot-sauce", "dragon ball", "peperoni")

# using arbitrary keyword arguments


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile


profile_1 = build_profile(
    "Frank", "Alimimian", location="nigeria", age=30, field="computer science"
)

print(profile_1)
