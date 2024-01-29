#https://realpython.com/beautiful-soup-web-scraper-python/https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup

url ="https://realpython.github.io/fake-jobs/"

page = requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

#Find elements by id

results=soup.find(id="ResultsContainer")
#print (results.prettify())

#Find elements by class Name
job_elements = results.find_all("div",class_="card-content")

print ("=================================================")

#get and print child elements
#for job_element in job_elements:
    #print(job_element, end="\n"*2)
 #   title_element = job_element.find("h2",class_="title")
  #  company_element = job_element.find("h3",class_="company")
   # location_element = job_element.find("p",class_="location")
    #print(title_element)
    #print(company_element)
    #print(location_element)
    #print()
print("===Extract text from HTML Elements \n\n =========")   
#Extract text from HTML Elements
for job_element in job_elements:
    #print(job_element, end="\n"*2)
    title_element = job_element.find("h2",class_="title")
    company_element = job_element.find("h3",class_="company")
    location_element = job_element.find("p",class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

