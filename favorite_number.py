# This program asks the user for their favorite number and stores it in a file.

from pathlib import Path
import json

prompt = "What's your favorite number? "
prompt += "Enter 'q' to quit. "

number = input(prompt)
path = Path("text_files/favorite_number.json")

if number != 'q':
    contents = json.dumps(number)
    path.write_text(contents)
elif number == 'q':
    print("Goodbye!")