person_0 = {
    'first_name': 'Warren', 
    'last_name': 'Buffett', 
    'age': 95, 
    'city': 'Omaha'
    }
person_1 = {
    'first_name': 'Charlie', 
    'last_name': 'Munger', 
    'age': 97, 
    'city': 'Los Angeles'
    }
person_2 = {
    'first_name': 'Bill', 
    'last_name': 'Gates', 
    'age': 65, 
    'city': 'Seattle'
    }

people = [person_0, person_1, person_2]

for person in people:
    print(f"{person["first_name"]} {person["last_name"]}" 
        "is a lengend in the world of business. "
        f"He is {person["age"]} years old and lives in {person["city"]}.")

# print(f"""
#     {person['first_name']} {person['last_name']} is a legend in the world of finance.
#     He is {person['age']} years old and lives in {person['city']}.
#     """)

