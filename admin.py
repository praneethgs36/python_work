"""A module that contains the Admin and Privilege classes. """
from user import User

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