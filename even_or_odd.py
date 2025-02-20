prompt = """
Tell me a number and I will tell you if it's even or odd. 
"""
number = int(input(prompt))

if number % 2 == 0:
    print(f"\nThe number {number} is even. ")
elif number % 2 != 0:
    print(f"\nThe number {number} is odd. ")