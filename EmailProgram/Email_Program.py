import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "pythoncodeine@gmail.com"
password = "pythoncodeine1"

class MessageUser():
    detale = []
    user_messages = []
    user_emails = []
    user_base_message = """ 
Witaj {name}!
Przyjezdzasz do mnie na herbate czy moze {amount}?

Jakbyś zapomniał dzisiaj jest: {date}.

Pozdrawiam,
Blazej Aksiutin - Junior Python Developer"""
    def add_user(self, name, amount, email=None):
        today = datetime.date.today()
        date = "{today.day}/{today.month}/{today.year}".format(today=today)
        detail = {
        "name" : name,
        "amount" : amount,
        "date" : date
        }
        if email is not None:
            detail["email"] = email
        self.detale.append(detail)
    def get_user(self):
        return self.detale
    def make_message(self):
        if len(self.detale) > 0:
            for element in self.get_user():
                message = self.user_base_message
                new_msg = message.format(
                    name = element["name"],
                    amount = element["amount"],
                    date = element["date"])
                emails = element.get("email")
                if emails:
                    user_data = {
                    "email" : emails,
                    "message" : new_msg
                    }
                    self.user_emails.append(user_data)
                else:
                    self.user_messages.append(new_msg)
            return self.user_messages
        return []
    def send_mail(self):
        self.make_message()
        if len(self.user_emails) > 0:
            for element in self.user_emails:
                user_em = element["email"]
                user_ms = element["message"]
                try:
                    email_con = smtplib.SMTP(host,port)
                    email_con.ehlo()
                    email_con.starttls()
                    email_con.login(username, password)
                    user_msg = MIMEMultipart("alternative")
                    user_msg["Subject"] = "Blazej Spam Developer!"
                    user_msg["From"] = username
                    user_msg["To"] = user_em
                    text = user_ms
                    part1 = MIMEText(text, "plain")
                    user_msg.attach(part1)
                    email_con.sendmail(username, [user_em], user_msg.as_string())
                    email_con.quit()
                except smtlib.SMTPException:
                    print("ERROR SENDING MESSAGE")
            return True
        return False



Object = MessageUser()
Object.add_user("Panie Bartku", "nie masz czasu", "pythoncodeine@gmail.com")
Object.add_user("Wojtek", "nie lubisz herbaty", "pythoncodeine@gmail.com")
Object.add_user("Zlotowlosy", "Jestes zajety", "pythoncodeine@gmail.com")
Object.add_user("Belgijski Polawiaczu Krewetek ", "Nie chce mi sie", "pythoncodeine@gmail.com")
Object.add_user("Developerze", "wypiles dzisiaj tyle herbaty, ze nie dy rydy wincej", "pythoncodeine@gmail.com")
Object.send_mail()







