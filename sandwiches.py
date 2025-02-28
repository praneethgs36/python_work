def sandwitch_maker(*ingredients):
    """Prints a summary of the sandwich ordered. """
    print("\nYour sandwich is made of: ")
    for ingredient in ingredients:
        print(f"{ingredient}")

sandwitch_maker('cheese', 'pasta', 'chicken')
sandwitch_maker('tomato')
sandwitch_maker('mozarilla', 'pepperoni')
