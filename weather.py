import requests

# Function to get weather data
def get_weather(city_name, api_key):
    base_url =  "http://127.0.0.1:5001"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    # Check if city is found
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]

        # Extracting data
        temp = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        description = weather["description"]
        wind_speed = wind["speed"]

        # Displaying the results
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        print(f"Wind speed: {wind_speed} m/s")
    else:
        print(f"City {city_name} not found!")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = "your_api_key" # here you enteryour api key
    city_name = input("Enter city name: ")
    get_weather(city_name, api_key)
