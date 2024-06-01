def display_message():
    """Display a simple message."""
    print("I am learning function")


display_message()


def favorite_book(title):
    """Display the user's favorite book."""
    print("One of my favorite book is " + title.title() + ".")


favorite_book("Richest man in babylon.")


def make_shirt(size="large", text="I love python"):
    """Display size and text of a shirt."""
    print(
        "Make your order of a T-shirt.\n\tSize: "
        + str(size)
        + "\n\tText: "
        + text
    )


make_shirt("XXL", "God is able")
make_shirt(size=12, text="Python is the best programming language!")
make_shirt("medium")
make_shirt("small", "Life is good...")

print("\n")
def describe_city(city, country):
    """Display a information about a city."""
    print(city.title() + " is in " + country.title())
    
describe_city("lagos","nigeria")
