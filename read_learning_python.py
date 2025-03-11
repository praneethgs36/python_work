from pathlib import Path

python_learnt_path = Path("C:/Users/Praneeth/Desktop/python_work/text_files/learning_python.txt")

python_learnt_contents = python_learnt_path.read_text().replace('Python', 'C')
print(f"{python_learnt_contents} \n")

# python_learnt_lines = python_learnt_path.read_text().splitlines()
# for line in python_learnt_lines:
#     print(line)
