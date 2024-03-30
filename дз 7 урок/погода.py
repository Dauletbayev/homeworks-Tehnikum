import requests
# from apikey import API_TOKEN
API_TOKEN = '3b55e2ff6e5dd329726472ab4724ffb4'

params = {'q': 'Ташкент', 'appid': API_TOKEN, 'units': 'metric'}
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
x = response.json()
weather = x['weather'][0]['main']
temp = x['main']['temp']

print(f'The weather in Tashkent is {weather}\n'
      f'The temperature is {temp} degrees')
