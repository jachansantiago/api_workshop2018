from twilio.rest import Client
import sys

msg = sys.argv[1]
# Your Account SID from twilio.com/console
account_sid = "<whiteboard>"
# Your Auth Token from twilio.com/console
auth_token = "<whiteboard>"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="<insert_your_number>",
    from_="<whiteboard>",
    body=msg)

print(message.sid)
