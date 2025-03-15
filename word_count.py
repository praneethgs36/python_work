"""This module defines the count_words function."""

from pathlib import Path

def count_words(file_location):
    """Count the approaximate number of words in a file. """
    path = Path(file_location)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"{file_location} not found in the given location. ")
        pass
    else:
        # count the number of words in the file
        words = contents.split()
        num_of_words = len(words) 
        print(f"The file path {file_location} has {num_of_words} words. ")
