# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# for topping in requested_toppings:
#     if topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {topping} to your pizza.")

# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

requested_toppings = ['mushrooms', 'french fries', 'pepperoni', 'extra cheese']
available_toppings = ['mushrooms', 'green peppers', 'pepperoni', 'pineapple',]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
