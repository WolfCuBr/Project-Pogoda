import requests

def get_weather_data(city):
    api_key = '9363ff679f205fbc3bdd6c89d71f9c0f'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    except requests.exceptions.RequestException:
        return None
