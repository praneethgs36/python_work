# fav_num = {'Aaron': 7, 'Bob': 3, 'Cathy': 9, 'Derek': 1, 'Evan': 5}
# for person in fav_num:
#     print(f"{person.title()}'s favorite number is {fav_num[person]}.\n")

fav_num = {
    'Aaron': [3, 7], 
    'Bob': [3, 5, 6], 
    'Cathy': [9], 
    'Derek': [1, 2], 
    'Evan': [5, 6, 1],
}

# print(fav_num)
for name in fav_num:
    if len(fav_num[name]) > 1: 
        print(f"\n{name.title()}'s favorite numbers are: "+ f"{[num for num in fav_num[name]]}")
        # for num in fav_num[name]:
        #     print(f"\t{num}") 
    elif len(fav_num[name]) <= 1: 
        print(f"\n{name.title()}'s favorite number is: " + f"{[num for num in fav_num[name]]}")
        # for num in fav_num[name]:
        #     print(f"\t{num}")