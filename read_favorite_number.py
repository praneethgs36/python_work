from pathlib import Path
import json

path = Path('text_files/favorite_number.json')
number = path.read_text()

contents = json.loads(number) 
print(f"I know your favorite number is {contents}! ")