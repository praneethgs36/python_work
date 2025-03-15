from pathlib import Path

path = Path('text_files/alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("File not found. ")
else:
    # count the number of words in the file
    words = contents.split()
    num_of_words = len(words) 
    print(f"The file path 'text_files/alice.txt' has {num_of_words} words. ")