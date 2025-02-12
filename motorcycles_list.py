motorcycles_list = ['honda', 'yamaha', 'suzuki']
#motorcycles_list[0] = 'ducati'
#print(motorcycles_list)
motorcycles_list.append('bmw')
# print(motorcycles_list)

motorcycles_list.insert(1, 'ktm')
#print(motorcycles_list)

#del motorcycles_list[0]
# print(motorcycles_list)

# burnt_motorcycle = motorcycles_list.pop(2)
# print(burnt_motorcycle)
# print(f"Your {burnt_motorcycle} has exploded. Choose another vehicle from your garage to continue the game. \nChoose one from the following list. ")
# print(motorcycles_list)

burnt_scooter = 'ktm'
motorcycles_list.remove(burnt_scooter)
print(motorcycles_list)