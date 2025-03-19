class Employee:
    """A class to represent an employee."""
    
    def __init__(self, first_name, last_name, salary):
            self.first_name = first_name
            self.last_name = last_name
            self.salary = salary

    def give_raise(self, raise_amount=5000):
        """Gives a raise to an employee's salary."""
        self.salary += raise_amount