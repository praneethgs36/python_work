"""A set of classes used to represent gas and electric cars. """

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

            self.odometer_reading += miles
        elif miles < 0:
            print("Your can't roll back the reading. ") 

class Battery:
    """Model the battery of an electric car. """
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes. """
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Display battery size description. """
        print(f"This car has a {self.battery_size}-kWh battery. ")

    def get_range(self):
        """Displays the details of the battery's range. """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} km on a full charge. ")

    def upgrade_battery(self):
        """Upgrades batter to 65 kwh if it isn't already. """
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a  car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then, initialize attributes specific to electric car. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()


