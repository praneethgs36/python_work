my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append("ice cream")

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# print(f"\nThe first three items in the list are {my_foods[:3]}.")
# print(f"The items from the middle of the list are {my_foods[1:4]}.")
# print(f"The last three items in the list are {my_foods[-3:]}.")

print("My favorite food items are:", )
for food in my_foods:
    print(food)

print("\nMy friend's favorite food items are:", )
for food in friend_foods:
    print(food)