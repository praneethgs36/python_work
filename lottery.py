"""Simulate a lottery win. """

from random import sample

characters = ['u', 'i', 'g', 'b', 9, 3, 2, 4, 6, 1, 7, 5, 4, 8]

# print(f"The winning ticket number is {winning_ticket}")

my_ticket = [9, 'g', 1, 'i']

trials = 0
while True:
    winning_ticket = sample(characters, 4)
    if winning_ticket == my_ticket:
        print("Congrats. You won!")
        trials += 1
        print(f"It took you {trials} trials for you to win!")
        break
    else:
        trials += 1
        