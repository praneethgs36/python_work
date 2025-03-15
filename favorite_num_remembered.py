# Accepts and return favorite number to the user. 

from pathlib import Path
import json

def retrieve_favorite_number(path):
    """Retrieve the favorite number if stored in a file."""
    
    number = path.read_text()
    contents = json.loads(number)
    return contents


def accept_favorite_number():
    """Accept the favorite number from the user and stores into a file."""
    
    prompt = "What's your favorite number? "
    prompt += "Enter 'q' to quit. "

    number = input(prompt)
    path_1 = Path("text_files/favorite_number_1.json")

    if number != 'q':
        contents = json.dumps(number)
        path_1.write_text(contents)
    elif number == 'q':
        print("Goodbye!")


def tell_favorite_number():
    """Tell the user their favorite number."""
    
    path_2 = Path('text_files/favorite_number_1.json')
    
    if path_2.exists():
        contents = retrieve_favorite_number(path_2)
        print(f"I know your favorite number is {contents}! ")
    else:
        accept_favorite_number()

tell_favorite_number()