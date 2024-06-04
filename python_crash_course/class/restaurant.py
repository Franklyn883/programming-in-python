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


class IceCreamStand(Restaurant):
    """Represent an aspect of a restaurant specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        """Initialize attributes specific to the parent class. Then initialize
        attributes specific to the an ice-cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Print all the flavor in the flavor's list."""
        for flavor in self.flavors:
            print(flavor)


Icecreamstand = IceCreamStand(
    "sizzlers", "ice-cream", ["vanilla", "cream", "apple-pie", "orange"]
)
Icecreamstand.display_flavors()