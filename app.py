from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city):
    api_key = 'weather_api_key' 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        weather_data = get_weather_data(city)
        if weather_data:
            weather_desc = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            return render_template('weather.html', city=city, weather_desc=weather_desc, temperature=temperature, humidity=humidity,wind_speed=wind_speed)
        else:
            return 'Error fetching weather data'
    else:
        return 'City parameter missing'

if __name__ == '__main__':
    app.run(debug=True)
