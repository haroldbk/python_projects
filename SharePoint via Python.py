#SharePoint via Python
#https://forms.office.com/r/3uedu6ddsa
import requests
import json

client_id ="291a2ec9-c1b5-4694-88ce-5c963e21957d"
client_secret = "Y73sGDu0mwi54cJtoZhE2E5n0Ln2Pzwa6j8Szr5ctVw="
tenant=  'taki'       #"https://taki.sharepoint.com"
tenant_id="48cad64c-af15-447c-ada5-f9988ded39f6"
client_id = client_id + '@'+tenant_id

data={
    'grant_type':'client_credentials',
    'resource': "00000003-0000-0ff1-ce00-000000000000/" + tenant + ".sharepoint.com@" + tenant_id, 
    'client_id':client_id,
    'client_secret':client_secret

}

headers = {
  'Content_type':'application/x-www-form-urlencoded'
}

url =  "https://accounts.accesscontrol.windows.net/tenant_id/tokens/OAuth/2"
r=requests.post(url,data=data,headers=headers)
json_data=json.loads(r.text)

print(json_data)
