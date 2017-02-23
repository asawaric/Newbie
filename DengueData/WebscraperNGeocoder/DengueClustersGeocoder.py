import googlemaps
from datetime import datetime
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyAIv-MJYdPseUVVyjsvrx8-I3q61jqDv2I')
colname = ['Location', 'Cases', 'Date']
data = pd.read_csv('DengueClusters.csv', names=colname)

Locations = data.Location.tolist()
Locations2 = Locations[1:]
Dates = data.Date.tolist()
LatLong = []
LatLong2 = []
Latitude = []
Longitude = []

# Geocoding an address
for i in Locations2:
    geocode_result = gmaps.geocode(i + ',Singapore')
    for j in geocode_result:
        LatLong.append(j['geometry'])
for k in LatLong:
    LatLong2.append(k['location'])
for elem in LatLong2:
    Latitude.append(elem['lat'])
    Longitude.append(elem['lng'])

Table = pd.DataFrame({'Locations' : Locations2,
                      'Latitude' : Latitude,
                      'Longitude': Longitude})
Table.to_csv('Geocodes.csv', index=False)
Table

