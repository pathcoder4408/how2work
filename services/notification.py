from twilio.rest import Client
from Products.MailHost.MailHost import MailHost
from plone import api

# Configuration (move to config.py)
TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_NUMBER = '+YourTwilioNumber'

def send_email(subject, recipient, body):
    mailhost = api.portal.get_tool(name='MailHost')
    mailhost.send(
        body,
        mto=recipient,
        mfrom="your-email@example.com",
        subject=subject,
        encode=None,
        immediate=False,
        charset='utf8',
        msg_type='text/html'
    )

def send_sms(body, to_number):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=TWILIO_NUMBER,
        to=to_number
    )

# Example function usage within workflow transitions or event listeners

