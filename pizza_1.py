def make_pizza(*toppings):
    """Print the list of toppings requested. """
    print("Making a pizza with the following toppings. ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('peppermint')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
