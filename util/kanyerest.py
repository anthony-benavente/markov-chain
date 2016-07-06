import requests
import json

r =  requests.get('http://www.kanyerest.xyz/api/album/the_life_of_pablo')

data = r.json()
for d in data['result']:
    print d['lyrics'].encode('ascii', 'ignore')