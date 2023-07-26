# Impmort modules
from flask import Blueprint
from controllers.createPostController import createPost
from controllers.getAllPostsController import getAllPosts
from controllers.getPostByIdController import getPostById
from controllers.deletePostController import deletePostById
from controllers.updatePostController import updatePOst

# Creation of a Blueprint for routes linked to posts
post_routes = Blueprint('post_routes', __name__)

# Define routes for each controller function

post_routes.route('/api/v1/posts', methods=['POST'])(createPost)
post_routes.route('/api/v1/posts', methods=['GET'])(getAllPosts)
post_routes.route('/api/v1/posts/<int:post_id>', methods=['GET'])(getPostById)
post_routes.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])(deletePostById)
post_routes.route('/api/v1/posts/<int:post_id>', methods=['PUT'])(updatePOst)