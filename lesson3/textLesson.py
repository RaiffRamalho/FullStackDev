from twilio.rest import Client

account_sid = "AC2a8df85472c477759f574af1d68aa08d"
auth_token = "1cb436df7d064942f38a77b466bd2e6a"
client = Client(account_sid, auth_token)

message = client.messages.create(
	body="Let's grab lunch at Milliways tomorrow!",
    to="+5583999691844",
    from_="+15402355704",
)

print(message.sid)