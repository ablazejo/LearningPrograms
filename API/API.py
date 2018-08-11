import requests

url ='https://api.yelp.com/v3/businesses/north-india-restaurant-san-francisco'

headers = {'Authorization': 'Bearer vjtB_7vK2mpVsUqheObKh7XXEvk3bOspArG-lxIKfExvPKKL7g_6KKmbKJ8fNBZ8aD8bniWUACB4IVBAyvgiYTsHePvwywVmzbImB6VAsvM2iN9YxsvRwTdildtuW3Yx'}
r = requests.get(url, headers=headers)
print(r.text)

#coś nie tak w funkcji, to u góry działa

def do_search(term = 'food', location='Newport Beach'):
    headers = {'Authorization': 'Bearer vjtB_7vK2mpVsUqheObKh7XXEvk3bOspArG-lxIKfExvPKKL7g_6KKmbKJ8fNBZ8aD8bniWUACB4IVBAyvgiYTsHePvwywVmzbImB6VAsvM2iN9YxsvRwTdildtuW3Yx'}
    term = term.replace(' ', '+')
    location = location.replace(' ', '+')
    base_url = 'https://api.yelp.com/v3/businesses/search'
    url = "{base_url}?term={term}&location={location}".format(
        base_url = base_url,
        term = term,
        location = location)
    print(url)
    params = {
        "term" : term,
        "location" : location
    }
    r = requests.get(url, headers=headers, params=params)
    return  r.json()

search1 = do_search()
print(search1)