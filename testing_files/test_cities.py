from city_functions import city_country

def test_city_country_pair():
    test_pair = city_country('santiago', 'chile')
    assert test_pair == 'Santiago, Chile - population '


def test_city_country_population():
    test_value = city_country('santiago', 'chile', 5000000)
    assert test_value == "Santiago, Chile - population 5000000"
    