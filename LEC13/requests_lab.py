import requests

params = {'City':'Seoul', 'name':'Suji'}

r = requests.get('https://httpbin.org/get', params=params)
r.status_code
r.url
r.headers['content-type']
r.json()

r.text