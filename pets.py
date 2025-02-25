# pet_0 = {'name':'britto', 'type': 'dog', 'owner': 'julie'}
# pet_1 = {'name':'morris', 'type': 'cat', 'owner': 'peter'}
# pet_2 = {'name':'jamie', 'type': 'gold fish', 'owner': 'susan'}

# pets = [pet_0, pet_1, pet_2]

# for pet in pets:
#     # print(pet)
#     print(f"{pet['name'].title()} is a {pet['type']} " 
#           f"owned by {pet['owner'].title()}. ")

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat'in pets:
#     pets.remove('cat')
# print(pets)

# def describe_pet(animal_type, pet_name):
#     """Display information about pets. """
#     print(f"\nI have a {animal_type}. ")
#     print(f"My {animal_type}'s name is {pet_name.title()}. ")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# def describe_pet(animal_type, pet_name):
#     """Display information about pets. """
#     print(f"\nI have a {animal_type}. ")
#     print(f"My {animal_type}'s name is {pet_name.title()}. ")

# describe_pet(pet_name='Harry', animal_type='hamster')

def describe_pet(pet_name, pet_age, animal_type='dog'):
    """Display information about pets. """
    print(f"\nI have a {animal_type}. "
        f"My {animal_type}'s name is {pet_name.title()}. "
        f"He is {pet_age} years old. ")

describe_pet('Willie', 5, 'hamster')