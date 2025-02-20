favorite_places = {
    'michael': ['new york', 'los angeles'], 
    'john': ['san francisco'],
    'jane': ['miami', 'denver', 'houston'],
    }

for name in favorite_places:
    print(f"\n{name}'s favorite places are: ")
    for place in favorite_places[name]:
        print(f"\t{place.title()}")