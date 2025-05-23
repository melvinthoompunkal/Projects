

# WeatherApp

A simple Flask web application to check the current weather by ZIP code or location name. It uses the [WeatherAPI.com](https://www.weatherapi.com/) to fetch real-time weather data and displays a weather icon alongside the temperature and condition.

---

# Features

* Input ZIP code or location name to get current weather.
* Displays temperature in Fahrenheit and weather condition.
* Shows a relevant weather icon based on the condition.
* Responsive, clean UI with a simple form.

---

# Technologies Used

* Python 3
* Flask
* HTML/CSS
* WeatherAPI.com (via HTTP API)
* Requests library
* dotenv for environment variable management

---

# Setup & Installation

### 1. Clone this repository

```bash
git clone https://github.com/melvinthoompunkal/WeatherAppProject.git
cd WeatherAppProject
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*(Create a `requirements.txt` with `Flask`, `requests`, `python-dotenv`)*

### 4. Get your WeatherAPI key

* Sign up at [WeatherAPI.com](https://www.weatherapi.com/)
* Obtain your API key

### 5. Create `.env` file (named `WeatherAPI.env` in your case) in the root directory

```env
WEATHER_API_KEY=your_actual_api_key_here
```

### 6. Run the Flask app

```bash
python app.py
```

### 7. Open your browser at

```
http://127.0.0.1:5000/
```

---

## Project Structure

```
weatherapp/
│
├── static/
│   ├── styles.css
│   └── Images/
│       ├── Clear.png
│       ├── Overcast.png
│       ├── Partly Cloudy.png
│       └── UnknownWeather.png
│
├── templates/
│   └── frontFlaskHTML.html
│
├── WeatherAPI.env
├── app.py
├── requirements.txt
└── README.md
```

---

## Code Overview

* **app.py**: Main Flask app that handles the GET and POST routes, calls WeatherAPI, and renders the HTML page with weather info and icon.
* **templates/frontFlaskHTML.html**: Contains the input form and display area for weather data.
* **static/styles.css**: CSS styling for the page.
* **static/Images/**: Folder with weather icons for display based on condition.

---

## Notes

* The app currently supports weather conditions: Clear, Overcast, Partly Cloudy (case-sensitive).
* Unknown or unsupported weather conditions will show a default icon (`UnknownWeather.png`).
* Temperatures are displayed in Fahrenheit but can be changed by adjusting the API query parameters.
* Make sure your API key has enough quota and is active.
* Add your own pictures to customize it!
---

## Future Improvements

* Add support for more weather conditions and icons.
* Enable metric units (Celsius).
* Show extended forecast.
* Improve error handling and validation for user input.
