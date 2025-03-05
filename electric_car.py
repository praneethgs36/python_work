"""A set of classes that can be used to represent electric cars. """
from car import Car


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

