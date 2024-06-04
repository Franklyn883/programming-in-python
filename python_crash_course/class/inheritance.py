from car import Car


class Battery:
    """A simple attempt to model an electrical car battery."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = (
            "This car can go approximately "
            + str(range)
            + " miles on a full charge."
        )
        print(message)

    def upgrade_battery(self):
        """Set the value of the size to a higher size."""
        if self.battery_size < 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes
        specific to an electric car."""
        super().__init__(make, model, year)

        self.battery = Battery()


my_electric_car = ElectricCar("tesla", "model s", 2016)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
print(my_electric_car.battery.battery_size)
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()

