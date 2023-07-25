# Impmort modules
from flask import Blueprint
from controllers.postControllers import createPost

# Creation of a Blueprint for routes linked to posts
post_routes = Blueprint('post_routes', __name__)

# Define a route for creating posts
post_routes.route('/api/v1/posts', methods=['POST'])(createPost)