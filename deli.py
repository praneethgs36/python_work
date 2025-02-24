sandwich_orders = ['pastrami', 
                   'tuna', 
                   'pastrami', 
                   'bacon', 
                   'pastrami', 
                   'cheese', 
                   'beef',
                   ]


finished_sanwiches = []

print("Pastrami is out of stock. ")

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        finished_sandwich = sandwich_orders.pop()
        print(f"Making {finished_sandwich} sandwich. ")
        finished_sanwiches.append(finished_sandwich)

print("\nThe following sandwich orders are ready to deliver:")
for sandwich in finished_sanwiches:
    print(sandwich)