
def make_sandwich(*items):
    """Print the summary of the sandwiches requested."""
    print("\nMaking your sandwich with the following items:")
    for item in items:
        print("\t adding " + item + " to your sandwich...")
    print("Your sandwich is ready")
    


make_sandwich("green pepper", "salad", "green beans", "pinch")
make_sandwich("green pea")


def build_profile(first, last, **user_info):
    """Returns an an object of a user information."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


frank = build_profile(
    "frank", "alimimian", age=31, field="computer science", country="nigeria"
)

print(frank)


def make_car(manufacturer, model_name, **car_info):
    """creates a dictionary containing everything we know about a car."""
    car_profile = {}
    car_profile["manufacturer"] = manufacturer
    car_profile["model"] = model_name

    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car_1 = make_car("toyota", "camry", price=150000, color="black")
print(car_1)


