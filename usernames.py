current_users = ['Afrin', 'Bobby', 'cathy', 'david', 'edward']
current_users_lower = [user.lower() for user in current_users]

new_users = ['frank', 'gabby', 'harry', 'afrin', 'bobby']

for new_user in new_users:
    if new_user in current_users_lower:
        print(f"Sorry username {new_user} is taken. Please pick another one.")
    else:
        print(f"Great! selected username {new_user} is available.")