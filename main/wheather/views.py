from django.shortcuts import render
import requests

# Create your views here.

def wheather(request):
    if request.method == 'POST':
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        print("this is latitude")
        print(latitude)
        
        
        WHEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'  
        parameters = {
            'lat': latitude,
            'lon': longitude,
            'appid': '7ed1d55db01178a46f7c7c097754fc0c'
        }

        response = requests.get(WHEATHER_ENDPOINT, parameters)
        weather_data = response.json()
        weather_list = [ forecast for forecast in weather_data['list']]
        location = weather_data['city']
        print(location['name'])
        
        

        weather_dict = {
            'weather_info':weather_list,
            'place' : location
        }

        return render(request, "result.html", weather_dict)
    
    else:
        return render(request, "firstpage.html")




