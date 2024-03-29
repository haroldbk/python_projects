#API ACCESS TO NASA.GOV
#https://realpython.com/python-api/#authentication
import requests
import json
#endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
api_key="DheUEYNKJwgChtz9aYc53yXXOK4mQORlJBsxth3u"
#query_param={"api_key":api_key,"earth_date":"2020-07-01"}
query_param={"api_key":api_key }
response=requests.get(endpoint,params=query_param)

#print(response.json())

#write the data to a json file
output_file = 'd:\\apps\\nasaPhotos_latest.json'
with open(output_file,'w') as json_file:
    json.dump(response.json(), json_file, indent=4)