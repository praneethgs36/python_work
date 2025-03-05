user_0 = {
    'username': 'efermi', 
    'first_name': 'enrico',
    'last_name': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in user_0:
    print(f"\nKey: {key}")
    print(f"Value: {user_0[key]}")
