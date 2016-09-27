'''
Preprocessing code

Crawl all california zip codes from http://www.zipcodestogo.com/California/
Join with zipcodes.csv: Zip, Lat, Lng
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Crawl all california zip codes
zipcodesUrl = 'http://www.zipcodestogo.com/California/'
page = BeautifulSoup(urlopen(zipcodesUrl).read())
output = open('californiaZipcodes.txt', 'w')
zipcodes = set()

for link in page.findAll('a'):
  try:
    tmp = int(link.text)
    output.write(link.text)
    output.write('\n')
    zipcodes.add(link.text)
  except:
    pass

output.close()

# Join with zipcodes.csv
zipToLocationsFilename = 'zipLocation.csv'
locationsOutput = open('locations.csv', 'w')
with open(zipToLocationsFilename, 'r') as f:
  for line in f:
    if line.startswith('ZIP'):
      continue
    zipcode, latitude, longitude = line.strip().split(',')
    if zipcode in zipcodes:
      locationsOutput.write('%s,%s\n' % (latitude, longitude, ))
  f.close()

locationsOutput.close()
