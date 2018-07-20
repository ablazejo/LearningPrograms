import csv
import shutil
from tempfile import NamedTemporaryFile

def edit_csv(file_path, id_edit=None, name=None, surname=None, age=None):
    tempfile = NamedTemporaryFile(delete=False, mode='w+')
    with open(file_path, "rt") as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'surname', 'age']      
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames, lineterminator = "\n")
        writer.writeheader()
        for row in reader:
            if id_edit is not None:
                if int(row['id']) == int(id_edit):
                    row['name'] = name
                    row['surname'] = surname
                    row['age'] = age
            else:
                pass
            writer.writerow(row)
        tempfile.close()
        shutil.move(tempfile.name, file_path)

edit_csv(file_path="obama.csv", id_edit=12, name="Donald", surname="Trump", age=64)