#Facebook_functions

#def fun(a,b):
   ###
   #else:
    #    return fun(a-1,a*b)
  ###
#r=fun(4,2)   
#print(f"results {r}")
from email.message import EmailMessage
import requests
#send email via smtp
import smtplib, ssl

url = "https://www.sefaria.org/api/calendars?year=2024&month=12&day=20"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
data=response.json()
print(data)

