from pathlib import Path
import json

username = input("What is your name? ")
contents = json.dumps(username)

path = Path('text_files/username.json')
path.write_text(contents)

print("Thanks for signing up {username}!" 
      "We will remember you when you return. ")