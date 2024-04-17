#Sefaria-Get Calendar send email via smtp
#https://developers.sefaria.org/reference/get_api-links-tref
#https://developers.sefaria.org/reference/get_api-calendars

from email.message import EmailMessage
import requests
#send email via smtp
import smtplib, ssl
year=input("enter a year: ")
month=input("enter a month: ")
day=input("enter the day: ")
url = f"https://www.sefaria.org/api/calendars?year={year}&month={month}&day={day}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
data=response.json()
#print(response.text)
calendar_items=data['calendar_items']
# Find the dictionary in calendar_items storing the metadata for Parashat Hashavua, 
# and save the ref, as well as the name of the week's Parasha.  
for item in calendar_items:    
    if "Parashat" in item['title']['en']:
    #if item['title']['en'] == 'Parashat Hashavua':
        parashat_description = item['description']['en']
print(parashat_description)



smtp_server = "smtp.ionos.com"

port = 587  # For starttls
sender_email = "haroldbk@estatesway.org"

receiver_email ="haroldbk@msn.com"
message=parashat_description.encode('ascii', 'ignore').decode('utf-8')

                          
#print(message)



#hk111382!
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()
msg=EmailMessage()
msg['from']=sender_email
msg.set_content(message)
msg['Subject'] ="parashat for this week"
msg['To']=receiver_email

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    #server.sendmail(sender_email,receiver_email,"just testing")
    server.send_message(msg=msg)
    #server.sendmail(sender_email,receiver_email,message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    print('message sent')
    server.quit()