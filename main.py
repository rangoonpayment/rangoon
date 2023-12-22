from twilio.rest import Client

# Your Twilio Account SID, Auth Token, and Twilio phone number
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

# Recipient's phone number
recipient_phone_number = 'recipient_phone_number'

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body='Hello, this is a test message!',
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print(f"Message SID: {message.sid}")
