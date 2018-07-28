import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://hoshinoya.com/en/'

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')
print(len(web_soup.findAll('img')))

driver = webdriver.Firefox()