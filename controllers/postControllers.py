# Import modules
from flask import jsonify, request
from models.Post import Post
from config.config import app, db

# Route for create a new post
@app.route('/api/v1/posts', methods=['POST'])

def createPost():
    # Retrieve JSON data from the request
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    author = data.get('author')

    isExistPost = Post.query.filter_by(title=title, body=body, author=author).first()
    if isExistPost:
        return jsonify({'message:' 'Post withe the same data already exists'}), 409

    new_post = Post(title=title, body=body, author=author)

    # Add the new Post object to the database session
    db.session.add(new_post)

    # Try to commit the transaction to the database
    try:
        db.session.commit()
        return jsonify({'message': 'The post was successfully created'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Error creating post.', 'details': str(e)}), 500


@app.route('/api/v1/posts', methods=['GET'])
def getAllPosts():
    posts = Post.query.all()
    result = []
    for post in posts:
        result.append({
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'author': post.author,
            'created_at': post.created_at,
            'updated_at': post.updated_at
        })
    return jsonify(result), 200