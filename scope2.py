from pprint import pprint
import googlemaps

API_KEY = 'AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ'

map_client = googlemaps.Client(API_KEY)

work_place_address = 'INSERT ADDRESS HERE'
response = map_client.geocode(work_place_address)
pprint(response)
print(response[0]['geometry'])