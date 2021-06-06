import json
from urllib import request
import googlemaps
apikey='AIzaSyAfNuHxsiXxo75YzVQHNB27OGXK0BBszHo'

gmaps = googlemaps.Client(key=apikey)

# Geocoding an address
geocode_result = gmaps.geocode('Warsaw')
aaaaaaaaa=1
print(geocode_result)
#radek siusiak
a=1
aleprovo=a+2