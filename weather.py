import api
import requests

#weather data retrival section

key = api.weather_key
def weather_response(city_name):
    api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+key
    json_data = requests.get(api_link).json()
    # print(json_data)
    weather_condition = json_data['weather'][0]['main']
    temp = str(int(json_data['main']['temp']-273.15))

    final_result = "and the present weather condition of "+city_name+" is "+weather_condition+" and the temprature is "+temp+" deg. C"
    return final_result

# print(weather_response('allahabad'))


#message processing part



#telebot section

