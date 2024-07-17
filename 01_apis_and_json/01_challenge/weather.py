# ここにコードを書いてください
import requests
from datetime import datetime, timedelta

API_KEY = "05203c3a4a9f0f67d9bb47dc3b00699a"
BASE_URL = "https://api.openweathermap.org"

def search_city(query):
    url = f"{BASE_URL}/geo/1.0/direct?q={query}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        cities = response.json()
        if not cities:
            print("City not found. Please try again.")
            return None
        if len(cities) > 1:
            print("Multiple matches found, which city did you mean?")
            for i, city in enumerate(cities, 1):
                print(f"{i}. {city['name']},{city['country']}")
            choice = int(input("> ")) - 1
            return cities[choice]
        return cities[0]
    else:
        print("Error occurred while searching for the city.")
        return None

def weather_forecast(lat, lon):
    url = f"{BASE_URL}/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecasts = {}
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).date()
            if date not in forecasts:
                forecasts[date] = {
                    'weather': item['weather'][0]['main'],
                    'temp': item['main']['temp_max']
                }
        return [{'date': date, **forecast} for date, forecast in list(forecasts.items())[:5]]
    else:
        print("Error occurred while fetching weather forecast.")
        return None

def main():
    while True:
        try:
            query = input("City?\n> ")
            city = search_city(query)
            if city:
                print(f"Here's the weather in {city['name']}")
                forecast = weather_forecast(city['lat'], city['lon'])
                if forecast:
                    for day in forecast:
                        print(f"{day['date']:%Y-%m-%d}: {day['weather']} {day['temp']:.1f}°C")
        except KeyboardInterrupt:
            print("\nThank you for using the weather CLI. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()