import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "clarcksmark@gmail.com"
receiver_email = "bertdert21@gmail.com"
password = "clarksmark54"

message = MIMEMultipart("alternative")
message["Subject"] = "spam "
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message


text = """\

"""
html = """\
<html>
  <body>
    <p>test<br>
       
    </p>
  </body>
</html>
"""

for i in range(5):

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )