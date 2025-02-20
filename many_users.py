users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username in users:
    print(f"\nUsername: {username}")
    # print(users[username])

    full_name = (users[username])['first'] + " " + (users[username])['last']
    print (f"Name: {full_name}")
    
    location = (users[username])['location']
    print(f"Place: {location}")
