import phonenumbers
import opencage
import folium
from myNumber import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumber import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_mumber(service_provider, "en"))

from opencage.geocoder import openCageGeocode

key = ''

geocoder = openCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat. lng], popup = location).add_to(myMap)

myMap.save("mylocation.html")