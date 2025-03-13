"""
This program prompts the user for their name and
writes it on a text file. "
"""
from pathlib import Path

prompt = "Please enter you full name: "
name = input(prompt)

path = Path("text_files/guest.txt")
path.write_text(name)

