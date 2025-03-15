from pathlib import Path

path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[0:52]}... ... ...")
print(f"The length of pi_string is {len(pi_string)}")

# print(contents)