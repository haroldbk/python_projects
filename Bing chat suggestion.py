#Bing chat suggestion
import smtplib
# create an SMTP object and connect to the server
smtp = smtplib.SMTP(host="smtp.ionos.com", port=587)
# login to the server with your credentials
smtp.login("haroldbk@estatesway.org", "Ms111382!")
# send an email message
smtp.sendmail("haroldbk@estatesway.org", "haroldbk@msn.com")
# terminate the SMTP session and close the connection
smtp.quit()
