class Restaurant:
    """Model a restaurant. """
    
    def __init__(self, name, type):
        "Initialize basic attrabutes of the restaurant. "
        self.name = name
        self.type = type

    def describe_restaurant(self):
        """Displays the basic details of the restaurant. """
        print(f"The restaurant's name is {self.name}. ")
        print(f"It is a {self.type} restaurant. ")

    def open_restaurant(self):
        """Displays that the restaurant is open. """
        print(f"{self.name} is open now. ")

# restaurant = Restaurant('Emerald', 'continental')
# print(restaurant.name)
# print(restaurant.type)
# estaurant.describe_restaurant()
# restaurant.open_restaurant()

restaurant_1 = Restaurant('Hill Palace', 'Indian')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('BBQ Nation', 'Turkish')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Ming', 'Chinese')
restaurant_3.describe_restaurant()
