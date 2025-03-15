from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None    
    
def get_new_username(path):
    """Prompt for a new username."""
    
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We will rember you when you return, {username}!")

def greet_user():
    """Greet the user by name."""
    
    path_1 = Path('text_files/username.json')
    username = get_stored_username(path_1)
    
    if username:
        print(f"Welcome back {username}!")

    else:
        get_new_username(path_1)

greet_user()