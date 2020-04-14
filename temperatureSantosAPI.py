import requests
import pytemperature
import lightLevels

def temperature():
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=-23.9618&lon=-46.3322&appid=afd2b21ab78f1900dac25c02c4f5e4f6')
    json_object = r.json()
    kelvin = float(json_object['main']['temp'])
    celcius = round(pytemperature.k2c(kelvin))
    print("Temperatura em Santos:", celcius, "ºC")
    if celcius == 20:
        lightLevels.low_1()
    if celcius == 21:
        lightLevels.med_1()
    if celcius == 24:
        lightLevels.high_2()
    return celcius

temperature()
