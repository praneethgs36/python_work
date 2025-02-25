def format_name(first_name, last_name, middle_name=''):
    """Returns full name. """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

f_name = input("Enter your first name. ")
m_name = input("Enter your middle name. Press enter if not applicable. ")
l_name = input("Enter your last name. ")

musician = format_name(f_name, l_name, m_name)
print(musician)

