responses = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb? ")
    responses[name] = response
    next_round = input("Enter 'next' to start the poll for a new participant. "
                       "Type 'exit' if everyone completed the poll. ")
    if next_round == 'exit':
        polling_active = False

print("The poll is over...")
for name in responses:
    print(f"{name} wants to climb {responses[name]}. ")