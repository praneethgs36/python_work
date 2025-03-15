from pathlib import Path

path = Path("text_files/programming.txt")

contents = "I fucking love programming. \n"
contents += "I love creating new games. \n"
contents += "I also enjoy working with data. \n"

path.write_text(contents)