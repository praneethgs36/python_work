def format_name(first_name, last_name, middle_name=''):
    """Returns full name. """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

while True:
    print("Tell us your name. Enter 'quit' to leave the program. ")
    f_name = " "
    if f_name != 'quit':
        f_name = input("your first name. ")
        m_name = input("your middle name. Press enter if not applicable. ")
        l_name = input("your last name. ")
        print(f"Hello, {format_name(f_name, l_name, m_name)}")
    else:
        break
