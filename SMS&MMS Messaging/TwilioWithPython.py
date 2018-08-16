from twilio.rest import Client

account_sid = 'AC8144b96f3916a7458e23f56188ca451c'
auth_token = 'e236a93435f2d38672d0a9aa67770d94'
media_url = 'https://d1u5p3l4wpay3k.cloudfront.net/wowpedia/e/e6/WoW_icon.png'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there Yoooo!',
                              from_='+48732230556',
                              to='+48790275954'
                          )

print(message.sid)


message_data = client.messages.get(sid = 'SM4822dd99e13f4f33b1794ef5fef3bcf5')
print(message_data)
print(dir(message_data))

