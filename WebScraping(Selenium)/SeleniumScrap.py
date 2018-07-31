import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import shutil
import time

url = 'http://www.brentstirton.com/'

driver = webdriver.Firefox()
driver.get(url)

iterations = 0
while iterations < 2:
    html = driver.execute_script('return document.documentElement.outerHTML')
    html_soup = BeautifulSoup(html, 'html.parser')
    users = html_soup.findAll('img')
    images = []
    try:
        for element in users:
            src = element['src']
            images.append(src)
            print(src)
    except:
        pass
    current_path = os.getcwd()
    print(current_path)
    for img in images:
        try:
            file_name1 = os.path.basename(img)
            file_name2 = file_name1[0:-13]
            print(file_name2)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, 'Images', file_name2)
            with open(new_path, 'wb') as output_file:
                shutil.copyfileobj(img_r.raw, output_file)
            del img_r
        except:
            pass
    iterations += 1
    time.sleep(20)