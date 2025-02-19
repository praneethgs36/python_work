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
    full_name = f"{users[first]} {users[last]}"
    location = users[location]    