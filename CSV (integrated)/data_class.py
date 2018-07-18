import os
import csv
from Templates import templates
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import shutil
from tempfile import NamedTemporaryFile

host = "smtp.gmail.com"
port = 587
username = "pythoncodeine@gmail.com"
password = "pythoncodeine1"

path = "my_data.csv"
file_item_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

class User_Message():
    def read_data(self, user_id=None, email=None):
        filename = file_item_path
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            unknown_user_id = None
            unknown_email = None
            for row in reader:
                if user_id is not None:
                    if int(user_id) == int(row.get("id")):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get("email"):
                        return row
                    else:
                        unknown_email = email
            if unknown_user_id is not None:
                print ("User id {user_id} not found".format(user_id=user_id))
            if unknown_email is not None:
                print ("Email {email} not found".format(email=email))
        return None

    def render_message(self, user_id=None, email=None):
        user = self.read_data(user_id=user_id, email=email)
        template_path_txt = "txt_template.txt"
        template_path_html = "html_template.html"
        template_txt = templates.get_template(template_path_txt)
        template_html = templates.get_template(template_path_html)
        if isinstance(user, dict):
            context = user
            render_txt = templates.render_template(template_txt, context)
            render_html = templates.render_template(template_html, context)
            return render_txt, render_html
        else:
            return None

    def send_message(self, user_id=None, email=None):
        message_txt, message_html = self.render_message(user_id=user_id, email=email)
        try:
            email_con = smtplib.SMTP(host, port)
            email_con.ehlo()
            email_con.starttls()
            email_con.login(username, password)
            the_msg =MIMEMultipart("alternative")
            the_msg["Subject"] = "Billing Update!"
            the_msg["From"] = username
            the_msg["To"] = username
            part1 = MIMEText(message_txt, "plain")
            part2 = MIMEText(message_html, "html")
            the_msg.attach(part1)
            the_msg.attach(part2)
            email_con.sendmail(username, username, the_msg.as_string())
            email_con.quit()
            return True
        except smtplib.SMTPException:
            print("Error during sending email")


    def send_to_all(self):
        tempfile = NamedTemporaryFile(delete=False, mode='w+')
        filename = file_item_path
        with open(filename, "rt") as csvfile,tempfile:
            reader = csv.DictReader(csvfile)
            fieldnames = ['id', 'name', 'surname', 'email', 'amount', 'sent', 'date']      
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames, lineterminator = "\n")
            writer.writeheader()
            for row in reader:
                self.send_message(user_id=int(row["id"]), email=str(row["email"]))
                print("Message has been sent")
                row['sent'] = "Sent"
                writer.writerow(row)
            tempfile.close()
            shutil.move(tempfile.name, file_item_path)
        return True




