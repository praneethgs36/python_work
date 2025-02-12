guest_list = ['Benjamin Franklin', 'Charlie Munger', 'Albert Camus', 'Satoshi Nakamoto', 'Balaji Srinivasan']

# for guest_name in guest_list:
    # print(f"Dear {guest_name}, \nI am hosting a dinner party on the following monday. I am thinking about making you the guest of honor. Please join us.\n")

# print(f"Unfortunately, {guest_list[3]} could not make it to the party due to privacy concerns.")

guest_list[3] = 'Vitalik Buterin'
# print(guest_list)

# for guest_name in guest_list:
    # print(f"Dear {guest_name}, \nI am hosting a dinner party on the following monday. I am thinking about making you the guest of honor. Please join us.\n")

guest_list.append('Naval Ravikant')
guest_list.insert(-2, 'Patrick Colson')
guest_list.insert(3, 'Ray Dalio')

#for guest_name in guest_list:
    #print(f"Dear {guest_name}, \nI am hosting a dinner party on the following monday and Benjamin Franklin is coming from the dead. Please join us.\nP.S: Now that we have more guests, I have found a bigger and prettier table.\n")

#print(guest_list)

new_guest_list= guest_list[5:7]

for guests in new_guest_list:
    print(f"Dear {guests}, \nI really apprecite your thinking about attending a dinner party at my house. However, at the moment I am not in the best financial shape. For this reason, I have decided to reduce the number of guests to two. Since I am trying to learn blockchain programming now, I decided to include only the guests who are most relevant to that. Removing you from the list was a difficult decision. I know that for a man of your caliber, this would be easy to understand I know that I am the only person who is losing anything here by leaving your out from the list.\nRegards \nPraneeth\n\n")

removed_guests_list = guest_list[0:5]  # Guests from indices 0 to 4
removed_guests_list.append(guest_list[7])  # Add guest at index 7



# Print messages for removed guests
for removed_guest in removed_guests_list:
    print(f"Dear {removed_guest},\nDue to financial constraints, I had to cut down on the number of guests. But you are still invited. Please make it to the party!\nRegards,\nPraneeth\n\n")


# del guest_list[0:8]
# print(guest_list)

print(f"We have {len(guest_list)} people on our guests list.")

