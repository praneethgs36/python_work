class Car:
    """Representation of a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Display the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it. ")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value. 
        Reject backward changes. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        elif mileage < self.odometer_reading:
            print("You can't roll back the reading.")

    def increment_odometer(self, miles):
        """Add the given amount to odometer reading. Reject subtractions. """
        if miles >= 0:
            self.odometer_reading += miles
        elif miles < 0:
            print("Your can't roll back the reading. ") 

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-1000)
my_new_car.read_odometer()