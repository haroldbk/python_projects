#https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs/"

page = requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

print(soup.contents)
#print (page.text)
results=soup.find(id='ResultsContainer')

#print(results.prettify)

job_elements = results.find_all("div",class_="csrd-content")

for job_element in job_elements:
    print(job_element,end="\n"*2)