#using office365 client
#https://pypi.org/project/Office365-REST-Python-Client/
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.lists.collection import ListCollection
import msal


site_url = "https://taki.sharepoint.com/"
app_principal= {
    'client_id':'291a2ec9-c1b5-4694-88ce-5c963e21957d',
    'client_secret':'Y73sGDu0mwi54cJtoZhE2E5n0Ln2Pzwa6j8Szr5ctVw='   
}
credentials=ClientCredential(app_principal['client_id'],
                             app_principal['client_secret'])
ctx=ClientContext(site_url).with_client_credentials('291a2ec9-c1b5-4694-88ce-5c963e21957d','Y73sGDu0mwi54cJtoZhE2E5n0Ln2Pzwa6j8Szr5ctVw=')
#ctx=ClientContext(site_url).with_client_credentials(settings.get('user_credentials','haroldbk@taki.onmicrosoft.com'),
#                                                    settings.get('user_credentials',"hk111382!" ))
web= ctx.web
ctx.load(web)
ctx.execute_query()
list =web.lists()
#print("web title: {0}" .format(web.proerties['Title']))
