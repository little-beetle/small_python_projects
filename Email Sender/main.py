"""
This script sends an email using the SMTP protocol via Gmail.

For the script to work, tou need to install the app2.py file,
which contains the password variable with the password for the Gmail account.

You must also allow less secure apps to access your Gmail account
(https://myaccount.google.com/lesssecureapps)

Before running the script, make sure that the SSL library is configured
properly in your Python environment.

Author: V. Kovalchuk
"""


from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


# Settings of the sender, recipient and content of the letter
email_sender = ''
email_password = password
email_receiver = ''
subject = "Title"
body = """
        message text
        """

# Creating an EmailMessage object and configuring the contents of the list:
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)

# Creating context SSL
context = ssl.create_default_context()

# send message
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())