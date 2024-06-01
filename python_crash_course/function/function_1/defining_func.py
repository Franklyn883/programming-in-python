def greet(username):
    """display a simple greeting"""
    print("Hello," + username.title() + " how are you doing today")


greet("peter")

# positional arguments


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("dog", "rub")
