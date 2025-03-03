class User:
    """Details of a user """
    
    def __init__(self, first_name, last_name, age, nationality):
        """Initializes user attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def describe_user(self):
        """Displays user info"""
        print(f"The user's name is {self.first_name} {self.last_name}. "
              f"He is {self.age} years old and is from {self.nationality}. ")
        
    def greet_user(self):
        """Displays a personalized greeting """
        print(f"Hello {self.first_name}, Welcome. ")

user_0 = User('Micheal', 'Keaton', 55, 'United States')
user_0.describe_user()
user_0.greet_user()

user_1 = User('Jeff', 'Hardy', 40, 'Australia')
user_1.describe_user()
user_1.greet_user()

user_2 = User('David', 'Deutch', 65, 'United Kingdom')
user_2.describe_user()
user_2.greet_user()

