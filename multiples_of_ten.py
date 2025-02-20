prompt = """
Tell me a number and I will tell you 
if it's a multiple of ten.
"""
number = int(input(prompt))

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10")
elif number % 10 != 0:
    print(f"\nThe number {number} is not a multiple of 10")
