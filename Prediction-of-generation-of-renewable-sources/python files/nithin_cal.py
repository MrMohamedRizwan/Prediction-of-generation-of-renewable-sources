import math
from matplotlib import pyplot as plt
import requests
# Solar panel parameters
pv_rating = 250  # in watts
pv_efficiency = 0.8




url = f"https://api.open-meteo.com/v1/forecast?latitude=10.76&longitude=13&hourly=temperature_2m&timezone=Asia/Tokyo&limit=24"
response = requests.get(url)
data = response.json()
print(data)
temp_data = data["hourly"]["temperature_2m"]
one_day_temperature=temp_data[:24]
url1 = f"https://api.open-meteo.com/v1/forecast?latitude=10.76&longitude=13&hourly=relativehumidity_2m&timezone=Asia/Tokyo&limit=24"
response1=requests.get(url1)
data1=response1.json()
humidity=data1["hourly"]["relativehumidity_2m"]
one_day_humidity=humidity[:24]
url2 = f"https://api.open-meteo.com/v1/forecast?latitude=10.76&longitude=13&hourly=direct_normal_irradiance&timezone=Asia/Tokyo&limit=24"
response2=requests.get(url2)

data2=response2.json()
irraditon=data2["hourly"]["direct_normal_irradiance"]
one_day_irraditon=irraditon[:24]
one_day_humidity=humidity[0:24]
one_day_temperature=temp_data[0:24]






# Environmental factors
# temperature = 25  # in Celsius
# humidity = 60  # in percentage

# Constants
k = 1.38e-23  # Boltzmann constant
q = 1.6e-19  # electron charge
t_abs = 298.15  # absolute temperature, in Kelvin
a = 1.2e-5  # temperature coefficient of voltage, in volts/Celsius
b = -0.35  # temperature coefficient of current, in %/Celsius
e = 0.85  # diode quality factor
output=[None] * 24
time=[]

for i in range(0,24):

    temperature = one_day_temperature[i]  # in Celsius
    humid = one_day_humidity[i]  # in percentage


# Solar irradiance calculation
    solar_irradiance = one_day_irraditon[i]  # in watts/m^2, assume a clear sunny day
    air_mass = 1 / math.cos(math.radians(60))  # assume sun altitude of 30 degrees

# Calculate solar cell temperature
    t_cell = temperature + (solar_irradiance / 800) * (25 - temperature)

# Calculate maximum power point voltage and current
    v_mp = (pv_rating / pv_efficiency) * (0.4 + (temperature - 25) * a)
    i_mp = (pv_rating / pv_efficiency) * (1 + b * (t_cell - 25)) / e

# Calculate the output power
    p_out = v_mp * i_mp

    print("Solar irradiance: {:.2f} W/m^2".format(solar_irradiance))
    print("Maximum power point voltage: {:.2f} V".format(v_mp))
    print("Maximum power point current: {:.2f} A".format(i_mp))
    print("Output power: {:.2f} kW".format(p_out/1000))
    output[i]=p_out
plt.plot(output)
plt.show()