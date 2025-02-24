# pet_0 = {'name':'britto', 'type': 'dog', 'owner': 'julie'}
# pet_1 = {'name':'morris', 'type': 'cat', 'owner': 'peter'}
# pet_2 = {'name':'jamie', 'type': 'gold fish', 'owner': 'susan'}

# pets = [pet_0, pet_1, pet_2]

# for pet in pets:
#     # print(pet)
#     print(f"{pet['name'].title()} is a {pet['type']} " 
#           f"owned by {pet['owner'].title()}. ")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat'in pets:
    pets.remove('cat')
print(pets)
