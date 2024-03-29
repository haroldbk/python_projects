#CuurencyScoop
#https://currencybeacon.com/
import requests
import json

endpoint = "https://api.currencybeacon.com/v1/convert"
api_key="48d4e482009962403c2692e823cc1855"

cFrom =  input('convert from? ')
cTo=input('convert to ')
cAmount=input("amount to convert ")


query_param={"api_key":api_key,"from":cFrom,"to":cTo,"amount":cAmount}
response=requests.get(endpoint,params=query_param)

val=response.json()
amount = val['response']['value']

print(f"convert USD to CAD for the amount 100 the value is {amount}")
