#Another Facebook example
import requests
from bs4 import BeautifulSoup

url ="https://realpython.github.io/fake-jobs/"

link_array =[]

response = requests.get(url)

if response.status_code==200:
    #extract HTML content and print it
    html_content = response.text
    print(html_content)
    print("html_content end")

    soup = BeautifulSoup(html_content,"html.parser")
    
    links= soup.find_all("a")
    if links:
        for link in links:
            link_array.append(link)
    else:
        print("nothing found")
else:
    print("Status code != 200")
print(len(link_array))
print("======================= \n\n ===========")
for link in link_array:
    print (link)

