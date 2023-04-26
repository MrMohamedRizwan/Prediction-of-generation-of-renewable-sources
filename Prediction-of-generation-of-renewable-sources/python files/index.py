from geopy.geocoders import Nominatim

try:
    geolocator = Nominatim(user_agent="MyApp")
    city=input("Enter the city ")
    location = geolocator.geocode(city)
    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)
except TypeError:
    print("Coordinates of "+ city + "is not found")