prompt = "Please enter your age. "
prompt += "Enter 'quit' to leave the program. "


active = True

while active:
    age_string = input(prompt)
    if age_string != 'quit':
        age = int(age_string)
        if age < 3:
            print("Your ticket is free. ")
        elif age <= 12:
            print("Your ticket costs $10. ")
        elif age > 12:
            print("Your ticket costs $15. ")
    else:
        break