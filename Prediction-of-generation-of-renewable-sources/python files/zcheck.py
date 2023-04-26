from pyowm.owm import OWM
from pyowm.utils import formatting,timestamps
from geopy.geocoders import Nominatim
import requests
import matplotlib.pyplot as plt
import datetime
import json

day=float(input())
API_KEY = "a624fb74-cff1-11ed-b59d-0242ac130002-a624fc6e-cff1-11ed-b59d-0242ac130002"
date_string = input("Enter a date and time (YYYY-MM-DD HH:MM): ")

    # Parse the date and time string into a datetime object
target_date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')
start = target_date
end = start + datetime.timedelta(hours=day)

    # Get solar irradiance data from Stormglass API
response = requests.get(
    f"https://api.stormglass.io/v2/solar/point?lat=18&lng=72&start={start}&end={end}&params=downwardShortWaveRadiationFlux",
    headers={"Authorization": API_KEY}
    )

data = response.json()['hours']
irradiances = [d['downwardShortWaveRadiationFlux'] for d in data]

    # Assume a fixed photovoltaic efficiency of 15%
pv_efficiency = 0.15

    # Calculate PV power in Watts
pv_powers = [irradiance['sg'] * pv_efficiency for irradiance in irradiances]

    # Plot PV power data
timestamps = [datetime.datetime.fromisoformat(d['time']).strftime('%m-%d %H:%M') for d in data]
plt.plot(timestamps, pv_powers)
plt.xlabel('Time')
plt.ylabel('PV Power (Watts)')
plt.title('PV Power Forecast for Your Area')
plt.show()