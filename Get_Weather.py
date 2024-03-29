#Get_Weather
#https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
#https://home.openweathermap.org/api_keys

import requests, json, math


api_key = "6f1505c81e7921b62040165a36397238"

#base url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#give city name
city_name = input("entr city name : ")
#complete_url variable to store
#complete url address
complete_url = base_url + "appid=" + api_key + "&q="+ city_name

# Get method requests module
# return response object
response = requests.get(complete_url)

#json method of response object
#convert json format data into python format data
x = response.json()

# Now x contains list of nested dictionaries
# check the value of "cod" key is equal to 
# a 404, means city is found otherwise, city is not found

if x["cod"] !="404":
    #store the value of "main" key in variable y
    y=x["main"]

    # store the value corresponding to the "temp" key of y 
    #this return Kelvin
    current_temperaturek = y["temp"]
    #convert to Fahrenheit and round to 2 decimal places
    current_temperature =round(((current_temperaturek-273.15) * 1.8)+32,2)

    # store the value of the pressure key of y
    # convert to psi 
    # 1 hpa = 0.0145037738
    hpa_conversion = 0.0145037738
    current_pressurehpa = y["pressure"]
    current_pressure = current_pressurehpa * hpa_conversion
    #print (current_pressure)
    # store the corresponding value of "hummidity" key of x
    current_hummidity = y["humidity"]

    #store the value of "weather " key in variable z
    z=x["weather"]

    # store the value corresponding to the "description" key at the 0th index of z
    weather_description = z[0]["description"]

    #print the following values
    print(" Temperature (in Fahreneheit unit): " +
         str(current_temperature) +
         "\n atmospheric pressue in (hpa unit): " +
         str(current_pressure) +
         "\n Humidity ( in percentage)" +
         str(current_hummidity) +
             "\n description = " +
             str(weather_description))
else:
    print(" City not found")

