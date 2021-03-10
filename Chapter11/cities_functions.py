city = input("what is the name of the city? ")
country = input("what is the name of the country? ")
population = input("what is the population? ")


def cities_function(city, country):
    full_name = f"{city} {country}"
    return full_name

def cities_function2(city, country, population):
    full_name = f"{city} {country} population: {population}"
    return full_name

cities_function(city, country)
cities_function2(city, country, population)