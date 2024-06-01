# Sometimes we may not know how many arguments will bee passed to our functions.
# to handle that we use arbitrary arguments.


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza("peperoni", "fresh sauce", "german tops")

# now let's use a for loop to nicely print everything in the tuple.


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("\t- " + topping)


make_pizza("peperoni", "hot-sauce", "dragon ball", "peperoni")
