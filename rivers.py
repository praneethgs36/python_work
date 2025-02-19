riv_count_dict = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

# for river in riv_count_dict:
#     country = riv_count_dict[river]
#     print(f"{river.title()} is the lifeblood of {country.title()}.")

print("The rivers are:")
for river in riv_count_dict.keys():
    print(river.title())

print("\nThe countries are:")
for country in riv_count_dict.values():
    print(country.title())