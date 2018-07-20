import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
base_url2 = 'https://www.yelp.com'
loc = 'Newport+Beach,+CA,+United+States'
current_page = 0


while current_page < 1:
    print(current_page)
    url = base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
        for biz in businesses:
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            print(title)
            first_line = ""
            try:
                address = biz.findAll('address')[0].contents
                for item in address:
                    if "br" in str(item):
                        pass
                    else:
                        first_line += item.strip(" \n")
                print(first_line)
            except:
                pass
            try:
                city = biz.findAll('span', {'class': 'biz-city'})[0].text
                print(city)
            except:
                pass
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[0].getText().strip(" \n\t\r")
            except:
                phone = None
            print(phone)
            html_address = biz.findAll('a', href=True, limit=1)
            for element in html_address:
                address = element['href']
                new_url = base_url2 + address
                print(new_url)
            yelp_2 = requests.get(new_url)
            yelp_soup2 = BeautifulSoup(yelp_2.text, 'html.parser')
            page = yelp_soup2.findAll('span', {'class': 'biz-website js-biz-website js-add-url-tagging'})
            correct=""
            if page:
                for item in page:
                    page_address = item.findAll('a')
                    print(page_address)
                    for el in page_address:
                        correct=el.findAll(text=True)
                        correct = str(correct)[2:-2]
                        print(correct)
            else:
                correct = "Sorry. No website"
                print(correct)
            print("")
            page_line = "NAME: {title}\nADDRESS: {address_1}\n{city}\nPHONE: {phone}\nWEBSITE: {website}\n\n".format(
                    title=title,
                    address_1=first_line,
                    city = city,
                    phone = phone,
                    website = correct
                )
            textfile.write(page_line)
    current_page += 1