"""A module that contains the restaurant class. """

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