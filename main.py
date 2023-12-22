from twilio.rest import Client

# Your Twilio Account SID, Auth Token, and Twilio phone number
account_sid = 'ACa000705d5520b9e2d8975b1a404248f6'
auth_token = '2f3b01dc2f7b23f58fe51322e23598d2'
twilio_phone_number = '+12057758770'

# Recipient's phone number
recipient_phone_number = '+959 449169428'

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body='Hello, this is a test message!',
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print(f"Message SID: {message.sid}")
