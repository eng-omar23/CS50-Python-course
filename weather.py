import requests

def get_weather_forecast(city):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == "404":
        print("City not found. Please check the city name.")
    else:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"Weather forecast for {city}:")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")

# Run the Weather Forecast App
city = input("Enter city name: ")
get_weather_forecast(city)
