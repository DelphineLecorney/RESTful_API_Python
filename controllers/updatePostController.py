# Import modules
from flask import jsonify, request
from models.Post import Post
from config.config import app, db
from utils.validations import isNonEmptyString

# Define a route to retrieve all items
@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])

#Function for update a post
def updatePOst(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)
    post.author = data.get('author', post.author)

    validations = {
        'title': isNonEmptyString,
        'body': isNonEmptyString,
        'author': isNonEmptyString
    }

    for i, validation in validations.items():
        if not validation(data.get(i)):
            return jsonify({'error': 'The title field is empty or invalid'})  


    try:
        db.session.commit()
        return jsonify({'message': 'The post was successfully updated'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':'Error updating post', 'details': str(e)}), 500
