from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# Replace this with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hussiii:hAyjS0Ny2do@mydb.ckxjdd4ew6cp.us-east-2.rds.amazonaws.com:5432/mydb' # Endpoint of RDS provided by AWS 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Tables 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Add other fields like email, password (hashed), etc.

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120), nullable=False)
    # Other fields like genre, Spotify ID, etc.

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

