from flask import Flask, request, jsonify, send_from_directory
import requests
import os
try:
    app = Flask(__name__, static_folder='C:/Users/Sanjana/Documents/Python')
except Exception:
    print("File not found!!!")

def get_weather_data(city):
    my_api = os.environ.get("API_KEY", "35f4e77c137e0108200f1ab75484e567")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception:
        return None

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    weather_data = get_weather_data(city)
    if weather_data:
        return jsonify({
            "name": weather_data["name"],
            "description": weather_data["weather"][0]["description"].capitalize(),
            "temperature": weather_data["main"]["temp"],
            "icon": weather_data["weather"][0]["icon"]
        })
    else:
        return jsonify({"error": "Could not retrieve weather data. Please check the city name."}), 404

if __name__ == '__main__':
    app.run(debug=True)
