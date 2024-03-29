#working with rest api
#https://realpython.com/api-integration-in-python/
import requests
api_url="https://jsonplaceholder.typicode.com/todos"
todo={"user_id":3, "title":"Buy Bread","completed":False}
response=requests.post(api_url,todo)
print(response.json())
print(response.status_code)
print(response.text)