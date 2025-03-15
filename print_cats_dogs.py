# Reads files and prints names of cats and dogs. 

from pathlib import Path

cat_path = Path('text_files/cats.txt')
dog_path = Path('dogs.txt')

try:
    print(f"Cats:\n{cat_path.read_text()}")
except FileNotFoundError:
    pass
try:
    print(f"Dogs:\n{dog_path.read_text()}")
except FileNotFoundError:
    pass