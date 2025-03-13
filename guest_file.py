"""
This program prompts the user for their name and
writes it on a text file. "
"""
from pathlib import Path
path = Path("text_files/guest_book.txt")
book =""
    
while True:
    prompt = "Please enter you full name. Enter 'q' if you want to quit: "
    name = input(prompt)
    if name == 'q':
        break
    else:
        book += name + '\n'
        path.write_text(book)
        print("Your name is added to the guests list. ")
