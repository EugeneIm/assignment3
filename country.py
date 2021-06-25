from hashlib import new
from data import countries_and_capitals
import random



class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        if population < population_minimum:
            raise ValueError(f'Popluation {population} is too low')
        self.population = population

        
        

countries = []

minimum_population = 2_000_000
population_minimum = 1_000_000
population_maximum = 1_000_000_000

for pair in countries_and_capitals:
    new_country = Country(name, capital, population).countries.append()
    population = random.randint(population_minimum, population_maximum + 1)
    countries.append(new_country)
    