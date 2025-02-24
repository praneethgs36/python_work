# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something and I will repeat it back to you. "
prompt += "\nType 'quit' to exit the program. "


message = " "
active = True
while active == True:
    message = input(prompt)
    if message != 'quit':
        print(message)
    elif message == 'quit':
        active = False
