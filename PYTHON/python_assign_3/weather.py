import requests

api_key = "886b5ec326b3640811b6765020a7330a" # Enter your API key here
api_url_base = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

def get_weather_data(city_name):
    api_url = api_url_base.format(city_name, api_key)
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        
        print(f"Current weather conditions in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Description: {weather_desc}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error retrieving weather data: {response.status_code}")

if __name__ == '__main__':
    city_name = input("Enter city name: ")
    get_weather_data(city_name)
