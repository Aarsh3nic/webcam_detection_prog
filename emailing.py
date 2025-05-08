import filetype
import smtplib
from email.message import EmailMessage
import os

PASSWORD = "YourPassword"  # os.getenv("PASSforsecondarygmail")
SENDER = "SenderEmail"
RECEIVER = "ReceiverEmail"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
        kind = filetype.guess(content)

    if kind is None or kind.mime.split('/')[0] != 'image':
        raise ValueError("Not a valid image file")

    email_message.add_attachment(
        content,
        maintype="image",
        subtype=kind.extension  # like 'jpeg', 'png', etc.
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_message.as_string())

    print("Email Sent")
