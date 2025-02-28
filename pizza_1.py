def make_pizza(size, *toppings):
    """Print the list of toppings requested. """
    print(f"\nMaking a {size}-inch pizza with the following toppings. ")
    for topping in toppings:
        print(f"- {topping}")