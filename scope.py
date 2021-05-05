import json 
import googlemaps
from pprint import pprint
import urllib.request
import urllib.parse
import requests
from PIL import Image


url = 'https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ&center=-74.8871479081073,121.44776220633602&zoom=0&format=png&maptype=roadmap&style=element:geometry%7Ccolor:0x212121&style=element:labels.icon%7Cvisibility:off&style=element:labels.text.fill%7Ccolor:0x757575&style=element:labels.text.stroke%7Ccolor:0x212121&style=feature:administrative%7Celement:geometry%7Ccolor:0x757575&style=feature:administrative.country%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&style=feature:administrative.land_parcel%7Cvisibility:off&style=feature:administrative.locality%7Celement:labels.text.fill%7Ccolor:0xbdbdbd&style=feature:poi%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:poi.park%7Celement:geometry%7Ccolor:0x181818&style=feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:poi.park%7Celement:labels.text.stroke%7Ccolor:0x1b1b1b&style=feature:road%7Celement:geometry.fill%7Ccolor:0x2c2c2c&style=feature:road%7Celement:labels.text.fill%7Ccolor:0x8a8a8a&style=feature:road.arterial%7Celement:geometry%7Ccolor:0x373737&style=feature:road.highway%7Celement:geometry%7Ccolor:0x3c3c3c&style=feature:road.highway.controlled_access%7Celement:geometry%7Ccolor:0x4e4e4e&style=feature:road.local%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:transit%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:water%7Celement:geometry%7Ccolor:0x000000&style=feature:water%7Celement:labels.text.fill%7Ccolor:0x3d3d3d&size=480x360'
MAP_URL= "https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ&center=39.8729,75.2437=17&zoom=12&size=4000000x4000000&maptype=satellite&markers=color:black|label:|PhiladelphiaAirport"

API_KEY= 'AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ'
city= 'Philadelphia'
zoom= 14
size= '500x500'
git p
#URL2= MAP_URL + "center =" + city + "&zoom=" + str(zoom) + "size = &500x500&key="  + API_KEY
response = requests.get(MAP_URL)

with open ('Philadelphia.png','wb') as file:
    file.write(response.content)
    file.close()
    img= Image.open('Philadelphia.png')
    img.show()


#map_client= googlemaps.Client(API_KEY)

#map_client = googlemaps.Client(API_KEY)

#airport_address = '800 Essington Ave, Philadelphia, PA'
#response = map_client.geocode(airport_address)

#response2 = urllib.request.urlopen(url)
#url_map=response2.read()




#pprint(response)
#print(response[0]['geometry'])
#print (url_map)

#with open ("API.json") as file:
 #   data=json.load(file)
  #  print(data)
