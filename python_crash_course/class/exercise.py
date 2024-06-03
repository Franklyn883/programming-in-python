class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        """Set the number_served to the given value."""
        self.number_served = number

    def increment_number_served(self, number):
        """Add the given value to number_served."""
        self.number_served += number

    def describe_restaurant(self):
        """Show the name of a restaurant ad the cuisine type."""
        print(self.name.title() + " cuisine: " + self.type.title())

    def open_restaurant(self):
        """Print message to indicate that the restaurant is open."""
        print(self.name.title() + " restaurant is open!")


restaurant = Restaurant("naija delight", "nigeria delicacies")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("home and away", "intercontinental dishes")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print(restaurant_1.number_served)

restaurant_1.set_number_served(25)
restaurant_1.increment_number_served(5)
print(restaurant_1.number_served)


class Users:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, password, country):
        """Initialize first name and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.country = country
        self.login_attempt = 0

    def increment_login_attempts(self):
        """Increases the value of login_attempt by 1."""
        self.login_attempt += 1
    def reset_login_attempts(self):
        """Reset the login_attempts to zero."""
        self.login_attempt = 0

    def describe_user(self):
        """Prints a summary of a user information"""
        print(
            "users details: \n"
            + "\tfirst name:"
            + self.first_name.title()
            + "\n\tlast name: "
            + self.last_name.title()
            + "\n\tCountry: "
            + self.country.title()
        )

    def greet_user(self):
        """Print a personalized greeting to users."""
        print("Hello " + self.first_name.title() + "!")


user_1 = Users(
    first_name="john", last_name="doe", password="john123", country="england"
)
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempt)
user_1.reset_login_attempts()
print(user_1.login_attempt)