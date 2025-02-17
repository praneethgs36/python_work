# printing odd numbers upto 20
# numbers_list= []
# for number in range(1,21,2):
#     numbers_list.append(number)
# print(numbers_list)

# # numbers upto 1 million
# numbers_list = []
# for number in range(1, 1000_001):
#     numbers_list.append(number)
# # print(numbers_list)
# print(min(numbers_list))
# print(max(numbers_list))
# print(sum(numbers_list))

# # list of multiples of 3 upto 30
# threes = []
# for number in range(3, 31, 3):
#     threes.append(number)
# print(threes)

# # list of cubes upto 10
# cubes= []
# for number in range(1,11):
#     cube= number**3
#     cubes.append(cube)
# print(cubes)

cubes = [number**3 for number in range(1, 11)]
print(cubes)