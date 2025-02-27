def greet_users(names):
    """Prints a greeting to each user in the list. """
    for name in names:
        message = f"Hello, {name.title()}"
        print(message)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
