import requests

def do_search(term =None, location=None):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer vjtB_7vK2mpVsUqheObKh7XXEvk3bOspArG-lxIKfExvPKKL7g_6KKmbKJ8fNBZ8aD8bniWUACB4IVBAyvgiYTsHePvwywVmzbImB6VAsvM2iN9YxsvRwTdildtuW3Yx'}
    params = {
        "term" : term,
        "location" : location
    }
    r = requests.get(url, headers=headers, params=params)
    return  r.json()

search1 = do_search(term='food', location='Newport Beach')
print(search1)

for i in search1['businesses']:
    print(i['name'])
    print(i.get('phone'))

