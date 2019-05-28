import logging

import requests

logging.basicConfig(level=logging.DEBUG)

URL = 'http://localhost:8000/api/'

# get token
r = requests.post(
    URL + 'token/',
    data={'username': 'user0', 'password': 'user0'}
)

token = r.json()['token']
headers = {'Authorization': 'Token ' + token}

# create element with a file (auth required)
r = requests.post(
    URL + 'element/',
    files={'file': open('Procfile', 'rb')},
    headers=headers
)

json = r.json()
shareable_link = json['shareable_link']
password = json['password']

# get stats, empty
r = requests.get(
    URL + 'stats/',
    headers=headers
)

print(r.json())

# request a secret file
r = requests.post(
    shareable_link,
    data={'password': password}
)

# file is present at
file_url = r.json()['file']

# get stats, empty
r = requests.get(
    URL + 'stats/',
    headers=headers
)

print(r.json())

# get file
r = requests.get(file_url)
print(r.content)
