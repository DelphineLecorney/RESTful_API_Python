import requests
import json

# File for test


url = 'http://127.0.0.1:5000/api/v1/posts'

posts_data = [
    {
        'title': 'My Title',
        'body': 'Body of the new post.',
        'author': 'Moi meme'
    },
    {
        'title': 'My second Title',
        'body': 'The second Body of the new post.',
        'author': 'Toujours moi meme'
    },
    {
        'title': 'My third Title',
        'body': 'The third Body of the new post.',
        'author': 'Encore moi meme'
    }
]

headers = {'Content-Type': 'application/json'}

for data in posts_data: 
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print('Post created successfully')
    elif response.json is not None:
        print('Error creating Post:', response.json)
    else:
        print('Error creating Post:', response.text)
