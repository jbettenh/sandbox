#! python 3
# This will request breweries from the Open Brewery DB
# https://www.openbrewerydb.org/documentation/01-listbreweries

import requests

brews= 'https://api.openbrewerydb.org/breweries'

resp = requests.get(brews)

if resp.status_code != 200:
    #This means something went wrong.
    raise requests.Apierror('GET /breweries/ {}'.format(resp.status_code))

for brewery in resp.json():
    print('{} {}'.format(brewery['id'], brewery['name']))


