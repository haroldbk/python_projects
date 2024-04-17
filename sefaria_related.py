#sefaria_related
#https://developers.sefaria.org/reference/get_api-related-tref
import requests
tref="Mishnah"
url="https://www.sefaria.org/api/ref-topic-links/Mishnah%20Peah%204%3A2"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
print("=====related====/n /n")
print(response.text)