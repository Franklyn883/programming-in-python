# Defining a function with optional arguments.
def get_formatted_name(first_name, last_name, middle_name=""):
    """Returns a neatly formatted full name."""

    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


footballer = get_formatted_name("frank", "alimimian", middle_name="osemudiamen")

print(footballer)

# using a function with a while loop

while True:
    print("\nTell me you name: ")
    print("(enter 'q) at any time to quit")

    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(first_name=f_name, last_name=l_name)
    print("\nHello, " + formatted_name + "!")
