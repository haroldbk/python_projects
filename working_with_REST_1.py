#working_with_REST_1
#https://realpython.com/api-integration-in-python/
import requests
api_url= "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()
print(response)