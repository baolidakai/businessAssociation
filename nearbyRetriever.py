'''
Please use python 3
Given a location, retrieve businesses nearby with Google Map API: https://developers.google.com/places/web-service/search

Supported types:
https://developers.google.com/places/supported_types

e.g.
https://maps.googleapis.com/maps/api/place/nearbysearch/json?radius=1000&types=bakery,bank,bar,beauty_salon,cafe,car_dealer,car_rental,car_repair,car_wash,clothing_store,convenience_sotre,department_store,electronics_store,florist,furniture_store,gas_station,hardware_store,home_goods_store,jewelry_store,movie_theater,pharmacy,restaurant,shoe_store,shopping_mall&key=[YOU_API_KEY]&location=51.507351,-0.127758


WARNING: The program might take some time to finish due to the limit bandwith for API
Please pause before each API request if you are writing your own code

TODO: Dump the retrieved results in a pickle set
'''

# Import libraries
from urllib.parse import urlencode
from urllib.request import urlopen
import json
import time
from collections import defaultdict
from geopy.geocoders import Nominatim
import codecs
from apriori import runApriori
import pickle

try:
  visited = pickle.load(open('visited.p', 'rb'))
except:
  visited = set()

try:
  apikey = open('credentials.txt').read().strip()
  serviceurl = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?radius=200&types=food&key={}&'.format(apikey)
except:
  print('Please put your google maps api key in credentials.txt')
  print('https://developers.google.com/places/web-service/search')
  exit()

fh = codecs.open('locations.csv', encoding = 'utf-8')
csvOutput = 'baskets.csv'
geolocator = Nominatim()
addrToBusiness = defaultdict(list)
newBasketCnt = 0
failCnt = 0
with open(csvOutput, 'a') as f:
  for line in fh:
    latitude, longitude = line.strip().split(',')
    if (latitude, longitude) in visited:
      # print('{}, {} retrieved before.'.format(latitude, longitude))
      continue
    time.sleep(0.1)
    url = serviceurl + urlencode({'location': '{},{}'.format(latitude, longitude)})
    js = json.loads(urlopen(url).read().decode())
    if js.get('status', None) in ['OK', 'ZERO_RESULTS']:
      print('Retrieving {} business near {}, {}'.format(len(js['results']), latitude, longitude, ))
      newBasketCnt += 1
      basket = [result['name'].split(',')[0] for result in js['results']]
      f.write('{},{},'.format(latitude, longitude))
      f.write(','.join(basket) + '\n')
      visited.add((latitude, longitude))
    else:
      failCnt += 1
      print('Unable to retrieve information from {}{}'.format(latitude, longitude))
  f.close()
print('{} locations added'.format(newBasketCnt))
print('{} locations failed'.format(failCnt))

pickle.dump(visited, open('visited.p', 'wb'))
print('Baskets are saved in {}'.format(csvOutput))
