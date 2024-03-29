#read text file and output to json file
import re
import json

with open('D:\\odLIve\\OneDrive\Drone shots\\Mini Pro 3\\2024\DJI_0429.SRT') as file:
    file_content = file.read()
    
 # Initialize an empty list to store location dictionaries
locations = []   
#extract latitude and longitude user regular expressions
pattern = r"\[latitude: ([\d.-]+)\] \[longitude: ([\d.-]+)\]"

matches = re.findall(pattern,file_content)

#create a list of dictionaries with latitude and longitude

#locations = [{'latitude': float(lat), 'longitude': float(lon)} for lat, lon in matches]
for lat,lon in matches:
    location={'latitude':float(lat), 'longitude':float(lon)}
    locations.append(location)
    
#write the data to a json file
output_file = 'locations.json'
with open(output_file,'w') as json_file:
    json.dump(locations, json_file, indent=4)
    
print(f"latitude and longitude values extracted and saved to {output_file}.")
    