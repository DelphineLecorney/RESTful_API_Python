# Import app object and database from config module
from config.config import app, db

# Import the post_routes blueprint from the routes.postRoutes module
from routes.postRoutes import post_routes as api_bp

app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)