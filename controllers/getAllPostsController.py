# Import modules
from flask import jsonify
from models.Post import Post
from config.config import app

# Define a route to retrieve all items
@app.route('/api/v1/posts', methods=['GET'])

# Function for display all the posts
def getAllPosts():
    # Retrieve all articles from the database
    posts = Post.query.all()
    result = []

    # Iterate through each item to transform it into a JSON object
    for post in posts:
        result.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'author': post.author,
            'created_at': post.created_at,
            'updated_at': post.updated_at
        })
    # Return item data as a JSON response with status code 200 (OK)
    return jsonify(result), 200