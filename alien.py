alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# alien_1 = {}
# alien_1["height"] = """
# 5'6"
# """
# print(alien_1['height'])

# new_points = alien_0['points']
# print(f"You have just earned {new_points} new points.")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

# print(alien_0)

# print(f"When the game started, the alien was {alien_0['color']}.")

# alien_0['color'] = "yellow"

# print(f"\nNow the alien is {alien_0['color']}.")

alien_0['speed'] = 'medium'

# The alien is moving to the right.
# Let's change its position based on its speed. 

# if alien_0['speed'] == 'slow':
#     alien_0['x_position'] = alien_0['x_position'] + 1
# elif alien_0['speed'] == 'medium':
#     alien_0['x_position'] = alien_0['x_position'] + 2
# elif alien_0['speed'] == 'fast':
#     alien_0['x_position'] = alien_0['x_position'] + 3

# print(f"""
# New postion of aliens is ({alien_0['x_position']}, {alien_0['y_position']})
# """)

del alien_0['points']
# print(alien_0)

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)