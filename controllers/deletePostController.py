from flask import jsonify
from models.Post import Post
from config.config import app, db
from utils.validations import confirmDelete

# Define a route to delete a post by its ID
@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])

# Check if the post with the given ID exists in the database
def deletePostById(post_id):
    # Retrieve the post from the database using the provided post_id
    post = Post.query.get(post_id)

    # Check if the post with the given ID exists in the database
    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    # Function for ensure to delete a post
    def delete_callback():

        try:
            db.session.delete(post)
            db.session.commit()
            return jsonify({'message': 'Post successfully deleted'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Error deleting post.', 'details': str(e)}), 500
        
    return confirmDelete('Are you sure to delete this post ?', delete_callback)
