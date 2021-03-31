from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACc05e97aa306494354bbdbda7b6d2b588"
# Your Auth Token from twilio.com/console
auth_token  = "<redacted>"

client = Client(account_sid, auth_token)

print("Enter a valid image url")

url = input()
to = "+<redacted>"

message = client.messages.create(
    to=to, 
    from_="+14049984082",
    body=url)

print("Message containing " + url + " sent to " + to + ".")
