from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automaker = {}
    for manf in data:
        automaker[manf['automaker']] = 0

    for model in data:
        if model['year'] == year:
            automaker[model['automaker']] = automaker.get(model['automaker']) + 1

    most_new_cars = max(automaker, key=automaker.get)

    return most_new_cars

def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    pass


print(most_prolific_automaker(1999))
