favorite_language = {
    'jen': ['python', 'rust'], 
    'sarah': ['c'], 
    'edward': ['rust', 'c++'], 
    'phil': ['python', 'haskell'],
    }

# print(favorite_language)

# language = favorite_language['edward'].title()
# print(f"Edward's favorite language is {language}.")

# for name in favorite_language:
#     language = favorite_language[name]
#     print(f"""
#         {name.title()}'s favorite language is 
#         {language.title()}.
#         """)

# friends = ['phil', 'sarah']
# for name in favorite_language:
#     print(f"\nHi {name.title()}.")
#     if name in friends:
#         print(f"I see you like {favorite_language[name]}")

# if "erin" not in favorite_language:
#     print("Erin, please take our poll!")

# for name in sorted(favorite_language):
#     print(f"{name.title()}, thank you for taking the poll.")

# print("The languages people like are:")
# for language in set(favorite_language.values()):
#     print(language.title())

lan = [
    'python', 
    'c', 
    'rust', 
    'python', 
    'java', 
    'c', 
    'c++', 
    'java', 
    'python', 
    'rust',
    ]
# print(lan)
# print(set(lan))

participants = list(favorite_language.keys())
# print(participants)

people = [
    'jen', 
    'sarah', 
    'edward', 
    'phil', 
    'aaron', 
    'bob', 
    'cathy', 
    'derek', 
    'evan',
    ]
# for name in people:
#     if name in participants:
#         print(f"Thank you {name.title()} for responding to our poll.")
#     elif name not in participants:
#         print(f"{name.title()}, Please take the poll.")

for name in favorite_language:
    if (len(favorite_language[name]) > 1):
        print(f"{name.title()}'s favorite languages are:")
        for language in favorite_language[name]:
            print(f"\t{language.title()}")
    else:
        print(f"{name.title()}'s favorite language is:")
        for language in favorite_language[name]:
            print(f"\t{language.title()}")

        