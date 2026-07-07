import os
from django.shortcuts import render
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def weather_home(request):
    weather_data = None
    hourly_forecast = []
    alerts_list = []
    error_msg = None
    
    API_KEY = os.getenv("WEATHER_API_KEY")
    # Defaut city if none searched yet
    city = "Okara" 

    if request.method == 'POST':
        city = request.POST.get('city', '').strip() or "Okara"

    # WeatherAPI se forecast aur alerts dono data mangwana (alerts=yes)
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=2&aqi=no&alerts=yes"
    
    try:
        response = requests.get(url).json()
        
        if 'error' not in response:
            current = response['current']
            location = response['location']
            forecast_day = response['forecast']['forecastday'][0]
            
            # 1. Base Weather Details
            weather_data = {
                'city': location['name'],
                'country': location['country'],
                'temp_c': round(current['temp_c']),
                'temp_f': round(current['temp_f']),
                'feels_like_c': round(current['feelslike_c']),
                'feels_like_f': round(current['feelslike_f']),
                'humidity': current['humidity'],
                'wind_kph': round(current['wind_kph']),
                'wind_mph': round(current['wind_mph']),
                'description': current['condition']['text'],
                'rain_chance': forecast_day['day']['daily_chance_of_rain'],
                'uv': current['uv'],
                'pressure': current['pressure_mb'],
                'sunrise': forecast_day['astro']['sunrise'],
                'sunset': forecast_day['astro']['sunset'],
            }
            
            # 2. Extract Alerts
            if 'alerts' in response and 'alert' in response['alerts']:
                for alert in response['alerts']['alert']:
                    alerts_list.append({
                        'headline': alert.get('headline'),
                        'severity': alert.get('severity'),
                        'desc': alert.get('desc'),
                        'expires': alert.get('expires')
                    })
            
            # 3. 24 Consecutive Hours Parsing
            all_available_hours = response['forecast']['forecastday'][0]['hour'] + response['forecast']['forecastday'][1]['hour']
            now_time = datetime.now()
            count = 0
            
            for hour_item in all_available_hours:
                item_time = datetime.strptime(hour_item['time'], '%Y-%m-%d %H:%M')
                if item_time >= now_time.replace(minute=0, second=0, microsecond=0):
                    if count < 24:
                        formatted_time = item_time.strftime('%I %p').lstrip('0')
                        if count == 0:
                            formatted_time = "Now"
                            
                        hourly_forecast.append({
                            'time': formatted_time,
                            'temp_c': round(hour_item['temp_c']),
                            'temp_f': round(hour_item['temp_f']),
                            'is_day': hour_item['is_day'],
                            'rain_chance': hour_item['chance_of_rain'],
                            'wind_kph': round(hour_item['wind_kph']),
                            'condition': hour_item['condition']['text']
                        })
                        count += 1
        else:
            error_msg = "City sahi se enter karein!"
    except Exception:
        error_msg = "Server se connect nahi ho pa raha."

    return render(request, 'weather_app/index.html', {
        'weather': weather_data, 
        'hourly': hourly_forecast, 
        'alerts': alerts_list,
        'error': error_msg
    })
