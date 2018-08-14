import requests

#DATA

username = 'AC8144b96f3916a7458e23f56188ca451c'
password = 'e236a93435f2d38672d0a9aa67770d94'

number_to_text = '+48790275954'
twilio_number = '+48732230556'

message_body = "Hi there, this is my first message from Twilio!"

#XML PARSER

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

#TO SEND MESSAGE

base_url = 'https://api.twilio.com/2010-04-01/Accounts'
message_url = 'https://api.twilio.com/2010-04-01/Accounts/' + username + '/Messages'

auth_cred = (username, password)

post_data = {
    "From": twilio_number,
    "To": number_to_text,
    "Body": message_body
}

#r = requests.post(message_url, data = post_data, auth=auth_cred)
#print(r.status_code)
#xml_pretty(r.text)

#TO CHECK STATUS OF MESSAGE

message_url_ind = message_url + '/SMe04e8a929f4449bb99fa8d01920fc273' #message_url + '/SID NUMBER'
get_r = requests.get(message_url, auth = auth_cred)
xml_pretty(get_r.text)