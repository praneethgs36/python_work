# Accepts two numbers from user and returns their sum

print("Here, you can add two numbers. Enter 'q' at any time to quit. ")
prompt_1 = "Enter the first number: "
prompt_2 = "Enter the second number: "


while True:
    num_1 = input(prompt_1)
    
    if num_1 == 'q':
        break
    else:
        num_2 = input(prompt_2)

        if num_2 == 'q':
            break
        else:
            try:
                sum_of_numbers = int(num_1) + int(num_2)
            except ValueError:
                print("Please enter valid numbers. ")
            else:
                print(f"The sum of {num_1} and {num_2} is {sum_of_numbers}. ")