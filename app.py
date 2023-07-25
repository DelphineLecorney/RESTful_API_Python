from flask import Flask
from config.config import app, db

from routes.postRoutes import post_routes as api_bp

from models.Post import Post

app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
