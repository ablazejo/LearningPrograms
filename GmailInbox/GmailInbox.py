import email
import imaplib
from bs4 import BeautifulSoup
import os
import mimetypes

username = 'pythoncodeine@gmail.com'
password = 'pythoncodeine1'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select('Inbox')

result, data = mail.uid('search', None, 'All')
inbox_item_list = data[0].split()
print(inbox_item_list)

# ~WAY TO FIND ONE ELEMENT~

# most_recent = inbox_item_list[-1]
# oldest = inbox_item_list[0]
# result2, email_data = mail.uid('fetch', oldest, 'RFC822')
# raw_email = email_data[0][1].decode('utf-8')
# email_message = email.message_from_string(raw_email)
# print(dir(email_message))
# print('')
# print(email_message['To'])
# payload = email_message.get_payload()
# print(payload)

# ~WAY TO FIND ALL ELEMENTS~
print("")
for element in inbox_item_list:
    result2, email_data = mail.uid('fetch', element, '(RFC822)')
    raw_email = email_data[0][1].decode('utf-8')
    email_message = email.message_from_string(raw_email)
    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    date_ = email_message['date']
    counter = 1
    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = part.get_filename()
        content_type = part.get_content_type()
        if not filename:
            ext = mimetypes.guess_extension(content_type)
            if not ext:
                ext = '.bin'
            if 'text' in content_type:
                ext = '.txt'
            elif 'html' in content_type:
                ext = '.html'
            filename = 'msg-part-%08d%s' %(counter, ext)
        save_path = os.path.join(os.getcwd(), "Emails", date_, subject_)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))
        counter += 1



