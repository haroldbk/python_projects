#send email with alternative rending options
#https://realpython.com/python-send-email/

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "haroldbk@estatesway.org"
receiver_email="haroldbk@msn.com"
password = input('type your password and press enter:')
message = MIMEMultipart("alternative")
message["Subject"] = "Just a new from home"
message["From"] = sender_email
message["To"]=receiver_email

#create the plain-text and HTML verion of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>HI George,</p>
<h2>This is the data:</h2>
<table style="border-collapse: collapse; width: 100%; height: 54px;" border="1">
<tbody>
<tr style="height: 18px;">
<td style="width: 25%; height: 18px;">
<h3>Name</h3>
</td>
<td style="width: 25%; height: 18px;">
<h3>City</h3>
</td>
<td style="width: 25%; height: 18px;">
<h3>Amount</h3>
</td>
<td style="width: 25%; height: 18px;">
<h3>type</h3>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 25%; height: 18px;">
<h4>Bob</h4>
</td>
<td style="width: 25%; height: 18px;">
<h4>Boston</h4>
</td>
<td style="width: 25%; height: 18px;">
<h4>34.56</h4>
</td>
<td style="width: 25%; height: 18px;">
<h4>Bush</h4>
</td>
</tr>
<tr style="height: 18px;">
<td style="width: 25%; height: 18px;">
<h4>Mary</h4>
</td>
<td style="width: 25%; height: 18px;">
<h4>Albany</h4>
</td>
<td style="width: 25%; height: 18px;">
<h4>56.11</h4>
</td>
<td style="width: 25%; height: 18px;">
<h4>flower</h4>
</td>
</tr>
</tbody>
</table>
<p>Get back to me ASAP,</p>
<p>&lt;sender&gt;</p>
  </body>
</html>
"""
part1=MIMEText(text,"plain")
part2=MIMEText(html,"html")
#Add HTML/plain-text parts to MIMEMultipart message
#the email client will try to render the last part first
message.attach(part1)
message.attach(part2)

#Create a secure connection with server and send email

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.ionos.com",465,context=context) as server:
    server.login (sender_email,password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    server.quit()
