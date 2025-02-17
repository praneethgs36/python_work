pizzas = ["Margherita", "Pepperoni", "Hawaiian", "BBQ Chicken"]

# for pizza in pizzas:
#     print(f"I don't know what a {pizza} looks like. For me, it's all just pizza.")
    
# print("\nI am not really into pizza. I prefer something healthy instead.")

friends_pizzas = pizzas[:]
pizzas.append("Supreme")
friends_pizzas.append("Vegetarian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)