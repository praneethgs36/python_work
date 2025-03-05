class Restaurant:
    """Model a restaurant. """
    
    def __init__(self, name, type):
        "Initialize basic attrabutes of the restaurant. "
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays the basic details of the restaurant. """
        print(f"The restaurant's name is {self.name}. ")
        print(f"It is a {self.type} restaurant. ")

    def open_restaurant(self):
        """Displays that the restaurant is open. """
        print(f"{self.name} is open now. ")

    def experience(self):
        """Displays the number of customers served. """
        print(f"The restaurant served {self.number_served} customers today. ")

    def add_customers(self, number):
        """Adds more customers to the restaurant's history. """
        self.number_served += number

class IceCreamStand(Restaurant):
    """Modelling an ice cream stand. """

    def __init__(self, name, type):
        """Initializing attributes in the parent class. """
        super().__init__(name, type)
        self.flavors = ['vanilla', 'butterscotch', 'chocolate', 'strawberry']

    def flavors_available(self):
        """Displays the ice cream flavors available. """
        print("The followng flavors are available. ")
        for flavor in self.flavors:
            print(flavor)

mikes_ice_creams = IceCreamStand("Mike's", 'Ice cream')
mikes_ice_creams.describe_restaurant()
mikes_ice_creams.flavors_available()

# restaurant = Restaurant('Emerald', 'continental')
# print(restaurant.name)
# print(restaurant.type)
# estaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant_1 = Restaurant('Hill Palace', 'Indian')
# restaurant_1.describe_restaurant()

# restaurant_2 = Restaurant('BBQ Nation', 'Turkish')
# restaurant_2.describe_restaurant()

# restaurant_3 = Restaurant('Ming', 'Chinese')
# restaurant_3.describe_restaurant()

# restaurant = Restaurant('Hill Palace', 'continental')
# restaurant.experience()
# restaurant.add_customers(100)
# restaurant.experience()
