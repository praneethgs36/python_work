def describe_city(city, country='United States'):
    """Identifies the country of a city. """
    print(f"{city.title()} is in {country.title()}. ")

describe_city('paris', 'france')
describe_city('New York')
describe_city('Amsterdam', 'Netherlands')