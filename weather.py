import requests

API_KEY = "your_api_key_here"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("Error:", data["message"])

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)
