from flask import jsonify
from models.Post import Post

# Function for retrieve post by ID
def getPostById(post_id):
    # Retrieve the post from the database by its ID
    post = Post.query.get(post_id)

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    return jsonify({
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'author': post.author,
        'created_at': post.created_at,
        'updated_at': post.updated_at
    }), 200
