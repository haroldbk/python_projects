import requests, uuid, json

def translate(source):
    # Add your key and endpoint
    key = "6b4c24b4779947af9aa3717124f7fb84"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "southcentralus"
    #location = "South Central US"

    path = 'translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'he',
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': source
    }]
  
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
        #print(response)
    
  
    return response


#results=translate('מבואר למי שעייאליהם בעבותות התחבולות הנפלאות תפקחנה בהם עיני עורי\' כל שכן עם מה שהישירה אל קנין השלמת זאת המשפחה המתעסקת בעניינים אלו ר"ל העבודה בקרבנות והסיר הטומאות החמורות והוא משפחת הכהנים וכדי שלא יחשוב אדם כי טומאת המת הוא מפני העפוש שהוא מזיק לקרובים אליו ביארה התורה שאפילו עצם אדם הוא מטמא זאת הטומאה החמורה אף על פי שאין בו עפוש והנה היתה יותר חמורה טמאת המים שיש בהם כדי הזאה  מטמאת המים שאין בהם כדי הזא')
#print(results)