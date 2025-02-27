message_list = ['Hey!', 'How are you?', "What's up!", 'Have a good day!']

def show_messages(messages):
    for message in messages:
        print(message)

# show_messages(message_list)

def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    return sent_messages

sent_messages = send_messages(message_list[:])
print(message_list)
print(sent_messages)
