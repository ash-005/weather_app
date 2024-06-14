# Weather App

This Weather App is a Flask-based web application that allows users to get current weather information for a specified location. It fetches weather data from an external API and displays it to the user.

## Project Structure
weather_app/
├── templates/
│   ├── index.html
│   └── weather.html
├── application.py
├── .gitignore
├── README.md
└── requirements.txt


## Features

- User-friendly interface to enter the location
- Fetches current weather information from a weather API
- Displays temperature, humidity, wind speed, and weather conditions


## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.7+
- Flask
- Requests


### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/ash-005/weather_app.git
   ```
2. Navigate to the project directory
```bash
cd weather_app
```
3. Create a virtual environment
```bash
python -m venv venv
```
4. Activate the virtual environment
```bash
venv\Scripts\activate
```
on macOS/Linux
```
source venv/bin/activate
```
5. Install the required packages
```bash
pip install -r requirements.txt
```

## Usage
- Obtain an API key from a weather data provider (e.g., OpenWeatherMap).
- Create a .env file in the project directory and add your API key:
  ```env
  WEATHER_API_KEY=your_api_key_here
  ```
- Run the Flask application
- Open your browser and go to http://127.0.0.1:5000/ to see the application in action.


### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeatures)
- Commit your changes (git commit -m 'Add some AmazingFeatures')
- Push to the Branch (git push origin feature/AmazingFeatures)
- Open a Pull Request
