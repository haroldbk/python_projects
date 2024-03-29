#get Access token
import msal
#client_id':'client_id':'291a2ec9-c1b5-4694-88ce-5c963e21957d',
#'client_secret':'Y73sGDu0mwi54cJtoZhE2E5n0Ln2Pzwa6j8Szr5ctVw='
client_id ="d24c911f-31e4-4977-a4a8-5612b3056430"
client_secret ="FxW8Q~pQuqf4PZHRyNcs8TAbkYTIFJf6VkJxsaG4"
tenant_id="48cad64c-af15-447c-ada5-f9988ded39f6"
authority=f"https://login.microsoftonline.com/{tenant_id}/oauth2"

app=msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority
)
result=app.acquire_token_for_client(scopes=["http://graph.microsoft.com/.default"])
access_token=result.get("access_token")
print(access_token)