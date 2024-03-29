#Get_ACCESS_token_MSGraph
import requests
request_body={
    #'username':'haroldbk@taki.onmicrosoft.com',
    #'password':"ms111382!",
    'client_secret':'mlt8Q~70fGOaUzTCnG7~Mc.trW.yAj6NkYTvpaND',
    'client_id':'1b8c3a08-88d5-4d76-bbeb-cd95670ecbec',
    'resource':'https://graph.microsoft.com',
    #'grant_type':'password'  
    'grant_type':'client_credentials'  
}

response=requests.post(url='https://login.microsoftonline.com/48cad64c-af15-447c-ada5-f9988ded39f6/oauth2/token',
                      data=request_body,headers={'content_type':'application/x-ww-form-urlencoded'} )

print(response.text)