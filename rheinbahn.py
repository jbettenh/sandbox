#! python 3

import requests

url = 'https://openservice-test.vrr.de/static02/XML_STOPFINDER_REQUEST?sessionID=0&requestID=0&language=DE&coordOutputFormat=WGS84&place_sf=kronprinzenstraße&placeState_sf=empty&type_sf=stop&name_sf=Lukaskirche&nameState_sf=empty&itdDateYear=2011&itdDateMonth=10&itdDateDay=24&itdTimeHour=11&itdTimeMinute=9&coordOutputFormatTail=0'

my_stop = requests.get(url)

print(my_stop.content)
