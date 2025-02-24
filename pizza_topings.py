# toppings = ['cheese', 'tomatoes', 'hot sauce', 'mozarilla', 'onions']
# for topping in toppings:
#     print(f"Adding {topping} to your pizza...")

prompt = ("Please tell us what toppings you want to add to your pizza. ")
prompt += ("Enter them one by one. ")
prompt += ("Enter 'quit' to stop adding toppings. ")

topping = " "
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"Adding {topping} to your pizza...")
    elif topping == 'quit':
        continue