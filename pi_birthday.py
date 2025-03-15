from pathlib import Path

path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

while True:
    birthday = input("Enter your birthday in the form of ddmmyy: ")
    if birthday in pi_string:
        print("Your birthday is in the first million digits of Pi. ")
    elif birthday not in pi_string:
        print("Your birthday is not in the first million digits of Pi. ")
