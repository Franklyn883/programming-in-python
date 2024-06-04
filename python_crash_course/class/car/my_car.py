from car import Car
my_new_car = Car("audi", "a4", 2016)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print(my_new_car.get_descriptive_name())