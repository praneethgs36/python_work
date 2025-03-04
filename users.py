class User:
    """Details of a user """
    
    def __init__(self, first_name, last_name, age, nationality):
        """Initializes user attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        """Displays user info"""
        print(f"The user's name is {self.first_name} {self.last_name}. "
              f"He is {self.age} years old and is from {self.nationality}. ")
        
    def greet_user(self):
        """Displays a personalized greeting """
        print(f"Hello {self.first_name}, Welcome. ")

    def increment_login_attempts(self):
        """Increases login attempts by 1. """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0. """
        self.login_attempts = 0

    def display_login_attempts(self):
        """Displays the number of login attempts. """
        print(f"You have tried {self.login_attempts} times to login. ")

class Admin(User):
    """Models an administrator of a website. """

    def __init__(self, first_name, last_name, age, nationality):
        """Initialize the attributes in the parent class. """
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = Privileges()

class Privileges:
    """Record the privileges of a user. """

    def __init__(self):
        """Initializing privileage attributes. """
        self.list = ['can add post', 
                    'can delete post', 
                    'can ban user',
                    'can delete the website',
                    ]
    def show_privileages(self):
        """Displays the list of privileges. """
        print("The user has the following privileges. ")
        for privilege in self.list:
            print(privilege)

admin_0 = Admin('Benedict', 'Cumberbatch', 40, 'Mexico')
admin_0.privileges.show_privileages()

# user_0 = User('Micheal', 'Keaton', 55, 'United States')
# user_0.describe_user()
# user_0.greet_user()

# user_1 = User('Jeff', 'Hardy', 40, 'Australia')
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User('David', 'Deutch', 65, 'United Kingdom')
# user_2.describe_user()
# user_2.greet_user()
# user_2.display_login_attempts()
# user_2.increment_login_attempts()
# user_2.display_login_attempts()
# user_2.reset_login_attempts()
# user_2.display_login_attempts()
