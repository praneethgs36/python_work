def format_name(first_name, last_name, middle_name=''):
    """Returns full name. """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


while True:
    print("Enter your name. Enter 'q' to exit the program at any stage. ")
    f_name = input("your first name. ")
    if f_name == 'q':
        break    
    m_name = input("your middle name. Just press enter if not applicable. ")
    if m_name == 'q':
        break
    l_name = input("your last name. ")
    if l_name == 'q':
        break
    print(f"Hello, {format_name(f_name, l_name, m_name)}")
