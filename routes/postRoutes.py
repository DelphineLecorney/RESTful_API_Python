# Impmort modules
from flask import Blueprint
from controllers.postControllers import createPost, getAllPosts, getPostById

# Creation of a Blueprint for routes linked to posts
post_routes = Blueprint('post_routes', __name__)

# Define a route
post_routes.route('/api/v1/posts', methods=['POST'])(createPost)
post_routes.route('/api/v1/posts', methods=['GET'])(getAllPosts)
post_routes.route('/api/v1/posts/<int:post_id>', methods=['GET'])(getPostById)
# post_routes.route('')