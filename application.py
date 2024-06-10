from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return f'Welcome to this weather API'

@app.route('/weather/<city>')
def get_weather(city):
    api_key = 'API KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        #print(weather_data)
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Weather data not available'})
    
if __name__ == '__main__':
    app.run(debug=True)
