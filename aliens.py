# alien_0_info = {'color': 'green', 'points': 5}
# alien_1_info = {'color': 'yellow', 'points': 10}
# alien_2_info = {'color': 'red', 'points': 15}

# aliens_info = [alien_0_info, 
#                alien_1_info, 
#                alien_2_info,
#                ]

# for alien_info in aliens_info:
#     print(alien_info)

import random

aliens = []
for x in range (30):
    alien_x_info = {
        'color': random.choice(['green', 'red', 'yellow']),
        'points': random.choice([5, 10, -7]),
        'speed': random.choice(['slow', 'medium', 'fast']),
        }
    aliens.append(alien_x_info)

print(f"The initial state of aliens is:\t")
for alien in aliens[0:10]:
    print(alien)
# print(f"\nA total of {len(aliens)} aliens are created.")

for alien in aliens[0:10]:
    if (alien['color'] == 'green') and (alien['speed'] == 'fast'):
        alien['color'] = 'yellow'
    elif (alien['color'] == 'yellow') and (alien['speed'] == 'fast'):
        alien['color'] = 'red'

print(f"\nThe modified state of aliens is:\t")
for alien in aliens[0:10]:
    print(alien)