# Count the number of times a word is repeated in a text file. 

from pathlib import Path

# sample = "Row, row, row your boat. Gently down the stream"
# print(sample.count('row'))

def word_rep_counter(file_location, word):
    path = Path(file_location)
    string_ = path.read_text()
    reps = string_.count(word)
    return reps

the_in_mobidick  = word_rep_counter('text_files/mobi_dick.txt', 'the ')
print(the_in_mobidick)