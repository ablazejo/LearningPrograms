import requests
import json
from bs4 import BeautifulSoup

#url = 'https://www.instagram.com/p/BVFkvmChgGx/?taken-by=bdolega'
url = 'https://www.instagram.com/p/Blh6hTVFkIR/?taken-by=daria_9o9_'
nickname = 'thehighlinetulum'

insta_req = requests.get(url)
insta_soup = BeautifulSoup(insta_req.text, 'html.parser')
body = insta_soup.find('body')
script = body.find('script')
raw_string = script.text.strip().replace('window._sharedData =', '').replace(';', '')
raw_load = json.loads(raw_string)
metrics = raw_load['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_comment']['edges'][0]['node']['owner']['username']
print(metrics)