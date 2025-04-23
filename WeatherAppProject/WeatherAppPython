from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="WeatherAPI.env")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_info = None
    image_file = None
    if request.method == "POST":
        zip_code = request.form['zipcode']
        api_key = os.getenv("WEATHER_API_KEY")
        url = "http://api.weatherapi.com/v1/current.json"
        params = {"key": api_key, "q": zip_code}

        try:
            response = requests.get(url, params=params)
            data = response.json()

            location = data["location"]["name"]
            temp = data["current"]["temp_f"]
            condition = data["current"]["condition"]["text"]

            weather_info = f"Weather in {location}: {condition}, {temp}°F"

            if condition in ["Clear", "Overcast", "Partly Cloudy", "Partly cloudy"]:
                if(condition  is "Partly cloudy"):
                    condition = "Partly Cloudy"
                image_file = f"Images/{condition}.png"
            else:
                image_file = "Images/UnknownWeather.png"

        except Exception as e:
            weather_info = f"Error: {e}" + ", add real location"

    return render_template("frontFlaskHTML.html", weather=weather_info, weather_image=image_file)


if __name__ == '__main__':
    app.run(debug=True)
    

