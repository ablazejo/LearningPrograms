from twilio.rest import Client

account_sid = ''
auth_token = ''
media_url = 'https://d1u5p3l4wpay3k.cloudfront.net/wowpedia/e/e6/WoW_icon.png'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there Yoooo!',
                              from_='',
                              to=''
                          )

print(message.sid)


message_data = client.messages.get(sid = '')
print(message_data)
print(dir(message_data))

