from pathlib import Path

path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[0:52]}... ... ...")
print(f"The length of pi_string is {len(pi_string)}")

# print(contents)