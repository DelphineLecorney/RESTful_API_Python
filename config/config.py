# Import modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating the Flask application instance
app = Flask(__name__)

# Configuring the MySQL database to use
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/api'

# Disable track changes to improve performance
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialization of the SQLAlchemy object to interact with the database
db = SQLAlchemy(app)
