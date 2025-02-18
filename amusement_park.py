# age = 12
# if age <=4:
#     print("Your admission is free.")
# elif age < 18:
#     print("Your ticket price is $20")
# else:
#     pirnt("Your ticket price is $40")

age = 45

if age < 4:
    price = "free"
elif (age < 18) or (age > 65):
    price = 20
elif age <= 65:
    price = 40

print(f"Your ticket cost is {price}.")
