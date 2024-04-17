#https://developers.sefaria.org/reference/tutorial-dvar-torah-outliner
import requests
import json

url = "https://www.sefaria.org/api/calendars"

# Make a GET request to the URL
response = requests.get(url)

# Parse the response as JSON
data = response.json()  

json_str=json.dumps(data,indent=4)

print(json_str)

# Retrieve the list of calendar_items
calendar_items=data['calendar_items']
# Find the dictionary in calendar_items storing the metadata for Parashat Hashavua, 
# and save the ref, as well as the name of the week's Parasha.  
for item in calendar_items:
    if item['title']['en'] == 'Parashat Hashavua':
        parasha_ref=item['ref']
        p_ref=parasha_ref
        parsha_name=item['displayValue']['en']
#print(f"parsha ref {parsha_ref} and the name is {parsha_name}")

#Selecting the First Verse
parasha_ref=parasha_ref.split(" ")[0]
print(parasha_ref)

#Retrieving the Parasha Text
url=f"https://www.sefaria.org/api/v3/texts/{parasha_ref}"

response=requests.get(url)

data=response.json()
#print(data)

he_vtitle=data['versions'][0]['versionTitle']
he_pasuk=data['versions'][0]['text']
print(he_vtitle)
print('\n\n')
print(he_pasuk)
print(parasha_ref)
#Retrieving a Different Edition of the Text
#get the English versin
url=f"https://www.sefaria.org/api/v3/texts/{parasha_ref}?version=english"

response=requests.get(url)

data=response.json()
#print(data)
# Retrieve the version title, and text for the English verse.
en_vtitle=data['versions'][0]['versionTitle']
en_pasuk=data['versions'][0]['text']
#print(en_vtitle)
#print('\n\n')
#print(en_pasuk)   

#Retrieving Parasha Commentaries
#url = f"https://www.sefaria.org/api/related/{p_ref}"
url = f"https://www.sefaria.org/api/ref-topic-links/{p_ref}"
# Make the GET request
response = requests.get(url)
response.raise_for_status()
if response.status_code != 204:
    retrn= response.json()
    print(retrn)
else:
# Parse the response as JSON
    data = response.json()
    
    json_str=json.dumps(data,indent=4)
#print("    Data \n\n")
print(json_str)
#We'll iterate through the links array in the response data, and append the ref (the citation) of all linked texts of type commentary to a list we'll call commentaries.
commentaries=[]
# Iterate through the "links" in our data response, filtering for commentary links, and 
# appending the text reference to our commentaries list. 
cal_items=data['calendar_items']

for cat_text in data['calendar_items']:
    if cat_text['category']=='Tanakh':
        commentaries.append(cat_text['displayValue'])

#Retrieving the Commentary Text
def get_commentary_text(ref):
    # Our standard GET request, and JSON parsing
    url=f"https://www.sefaria.org/api/v3/texts/{ref}"
    response= requests.get(url)
    data = response.json()
    

    # Checking to make sure we have a primary version for the commentary 
    # (otherwise, the versions field would be empty)
    if "versions" in data and len(data['versions'])>0:
            # Retrieve the general name of the commentary book (i.e. "Rashi on Genesis")
            title=data['title']
            # Retrieve the text of the commentary
            text = data['versions'][0]['text']
             # Return the title, and the text
            return title, text

#Now, we'll apply this function to the first three commentaries in our list of commentaries:
com1_title,com1_text=get_commentary_text(commentaries[0])
com2_title,com2_text=get_commentary_text(commentaries[1])
com3_title,com3_text=get_commentary_text(commentaries[2])

#We are ready for the final step, printing our outline!
print("\nThree Commentaries")
print(f"A) {com1_title}: {com1_text}\n")
print(f"B) {com2_title}: {com2_text}\n")
print(f"C) {com3_title}: {com3_text}\n")            
            
             