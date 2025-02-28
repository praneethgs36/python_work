def build_profile(first, last, **user_info):
    """Build a dictionary that contains the details of a user. """
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

# user_profile = build_profile('albert', 
#                              'einstein', 
#                              location='princeton', 
#                              feild='physics'
#                              ) 

# print(user_profile)

my_profile = build_profile('praneeth', 
                             'g s', 
                             location='chennai', 
                             feild='writing'
                             ) 

print(my_profile)

# def build_profile(**user_info):
#     """Build a dictionary that contains the details of a user. """
#     return user_info

# user_profile = build_profile(first='albert', 
#                              last='einstein', 
#                              location='princeton', 
#                              feild='physics'
#                              ) 

# print(user_profile)