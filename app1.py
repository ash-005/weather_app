from flask import Flask, render_template, request, url_for,redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/weather',methods = ['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        api_key = 'weather_api_key'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
        response = requests.get(url)
        #print(response)
        if response.status_code==200:
        #data = response.json()
            w_data = response.json()
            if w_data:
                weather_desc = w_data['weather'][0]['description']
                temperature = w_data['main']['temp']
                humidity = w_data['main']['humidity']
                wind_speed = w_data['wind']['speed']
                return render_template('index1.html',city=city, weather_desc=weather_desc, temperature=temperature, humidity=humidity,wind_speed=wind_speed)
            else:
                return 'Error fetching the data'
        else:
            return 'Error fetching weather data'
    else:
        return 'City Parameter Missing'
if __name__ == '__main__':
    app.run(debug=True)

