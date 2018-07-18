import csv
import os
import datetime

def get_id(file_path):
    with open(file_path, "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        reader_list = list(reader)
    return len(reader_list)


def print_header(file_path):
    fieldnames = ['id', 'name', 'surname', 'email', 'amount', 'sent', 'date']
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def reader(file_path):
    with open(file_path, "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)


def add_data(file_path, name, surname, email, amount, date):
    if not os.path.isfile(file_path):
        open(file_path, "w+")
    next_id = get_id(file_path)
    fieldnames = ['id', 'name', 'surname', 'email', 'amount', 'sent', 'date']
    if next_id == 0:
        print_header(file_path)
    today = datetime.date.today()
    date = "{today.day}/{today.month}/{today.year}".format(today=today)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writerow({
            'id' : next_id,
            'name': name,
            'surname': surname,
            'email' : email,
            'amount' : amount,
            'sent' : "assds",
            'date' : date,
            })
    reader(file_path)

add_data("my_data.csv", "Michael", "Obama", "pythoncodeine@gmail.com", 1342, 34)
