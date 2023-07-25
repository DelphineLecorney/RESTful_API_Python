import requests
import json

url = 'http://127.0.0.1:5000/api/v1/posts'

data = {
    'title': 'My Title',
    'body': 'Body of the new post.',
    'author': 'Moi même'
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print('Post created successfully')
else:
    print('Error creating Post', response.json())
