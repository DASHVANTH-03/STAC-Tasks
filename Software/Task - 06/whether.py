from flask import Flask, render_template,request,redirect
import requests

app = Flask(__name__)

try:
    def get_weather(city,country):
        whether_url = 'https://api.open-meteo.com/v1/forecast'
        loc_url = 'https://api.api-ninjas.com/v1/geocoding'
        loc_header = {"X-Api-Key":"d+vYIOu70bq4PeEf4FI+Iw==BmHXR7ZmaVBvXFTL"}
        loc_params = {"city":city,"country":country}
        loc = requests.get(loc_url,headers = loc_header,params = loc_params)
        loc = loc.json()[0]
        whether_params = {
        "latitude":loc["latitude"],
        "longitude":loc["longitude"],
        "hourly":["temperature_2m", "precipitation_probability"],
        "models": "best_match",
        "timezone":"auto",
        "forecast_days": 1,
        "forecast_hours": 24
        }
        return requests.get(whether_url,params=whether_params)

except :
    pass


@app.route('/',methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']
        weather_data = get_weather(city,country)
        return render_template('about.html')
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)