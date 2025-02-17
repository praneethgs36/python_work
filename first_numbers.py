for value in range(11,6):
    print(value)

print(list(range(6)))

# even numbers upto 4
print(list(range(0,6,2)))

# square numbers upto 10
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    
print(squares)

# list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)