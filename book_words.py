from word_count import count_words

files = ['text_files/alice.txt', 'siddhartha.txt', 'text_files/mobi_dick.txt']

for file in files:
    count_words(file)