from email.message import EmailMessage
import smtplib, ssl

smtp_server = "smtp.ionos.com"

port = 587  # For starttls
sender_email = "haroldbk@estatesway.org"

receiver_email ="haroldbk@msn.com"
message= f"Hi y'all, \nthis is a message from PYHON"


msg=EmailMessage()
msg['from']=sender_email
msg.set_content(message)
msg['Subject'] ="parashat for this week"
msg['To']=receiver_email

password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    #server.sendmail(sender_email,receiver_email,message)
    server.send_message(msg=msg)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()