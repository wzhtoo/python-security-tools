import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

trace_number = phonenumbers.parse(number)
location = geocoder.description_for_number(trace_number, "en")
print(location)


service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "cbd1811cb28e408499c6206a70d59096en"))

key = 'cbd1811cb28e408499c6206a70d59096'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")

