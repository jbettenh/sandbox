#! python 3
# This will request information from the Space X API

import requests

#url_spacex = 'https://api.spacexdata.com/v3/launches/latest?pretty=true'
url_spacex = 'https://api.spacexdata.com/v3/capsules'

mission = requests.get(url_spacex)

if mission.status_code != 200:
     # This means something went wrong.
    raise requests.HTTPError('GET /Latest/ {}'.format(mission.status_code))

# print(mission.content)
print('Serial ID    Status  Launch Date')
print('------------------------------------------------')
for capsule in mission.json():
    if capsule['capsule_id'] == 'dragon1':
        print('{} {} {} {}'.format(capsule['capsule_serial'], capsule['capsule_id'], capsule['status'], capsule['original_launch']))

