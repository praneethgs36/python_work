# user_names = ['admin', 'john', 'jane', 'joe', 'jim']
user_names = []

for user in user_names:
    if user == 'admin':
        print(f"Hello {user}. Would you like to see a status report?")
    else:
        print(f"Hello {user}. Welcome back!")

if user_names:
    print("We have someone usin our system.")
else:
    print("We need to find some users!")