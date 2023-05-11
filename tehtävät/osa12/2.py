import requests
API_KEY = 'secret'
city = input('Enter city name: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    temperature_celsius = temperature - 273.15
    weather = data['weather'][0]['description']
    print(
        f'The weather in {city} is {weather} and the temperature is {temperature_celsius:.1f}°C.')
else:
    print('Failed to get weather information.')
