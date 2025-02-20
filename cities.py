cities = {
    'hong kong': {
        'country': 'china', 
        'population': 5_000_000, 
        'fact': 'They have a CEO, not a president.'
    },
    'singapore': {
        'country':'singapore', 
        'population': 4_000_000, 
        'fact': 'When WWII ended, they were very poor.',
    }, 
    'Bern': {
        'country': 'switzerland', 
        'population': 1_000_000, 
        'fact': 'They have over 100 languages spoken in the city.',
    },
}

for city in cities:
    print(
    f"{city.title()} is a city in {(cities[city])['country']}. "
    f"It has a population of {(cities[city])['population']}. "
    f"{(cities[city])['fact']}"
    )