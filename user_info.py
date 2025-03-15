from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None    
    
def get_new_username(path):
    """Prompt the user for basic details and store them."""
    
    name = input("What is your name? ")
    place = input("Where are you from? ")
    age = input("How old are you? ")
    user_info = {'name': name, 'place': place, 'age': age}
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"We will rember you when you return, {name}!")

def greet_user():
    """Greet the user by name and tell them back their details."""
    
    path_1 = Path('text_files/user_info.json')
    path_2 = Path('text_files/user_info_1.json')
    user_info = get_stored_username(path_1)
    
    if user_info:
        prompt = f"Welcome back {user_info['name']}! Enter 'c' to continue. "
        prompt += f"\n Not {user_info['name']}? Enter 'n' to sign up . "
        user_input = input(prompt)
        
        if user_input == 'c':
            print(f"\nYou are from {user_info['place']} and "
              f"you are {user_info['age']} years old.")
            
        elif user_input == 'n':
            get_new_username(path_2)
    else:
        get_new_username(path_1)
greet_user()