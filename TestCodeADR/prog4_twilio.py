from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC76599655ef4cff24da32d615ac85d12b"
auth_token  = "da361dc4b6b9c40af56990193e72f465"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="ADi you are a walking carrot - un fel de banana cu mustati si putza",
    to="+447856934039",    # Replace with your phone number
    from_="+441599312045") # Replace with your Twilio number

print message.sid




