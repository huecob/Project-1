from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server import app

# Set the database URI and other configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///project1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define your models below...

class User(db.Model):
    """User Information"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}>"
    
class Weather(db.Model):
    """Weather data"""

    __tablename__ = "weathers"

    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weather_type = db.Column(db.String)

    playlists = db.relationship("Playlist", back_populates="weather")

class Playlist(db.Model):
    """Playlist Stuff"""

    __tablename__ = "playlists"

    playlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    playlist_name = db.Column(db.String)
    playlist_weather_id = db.Column(db.Integer, db.ForeignKey('weathers.weather_id'))

    weather = db.relationship("Weather", back_populates="playlists")
    songs = db.relationship("Song", back_populates="playlist")

class Song(db.Model):
    """Music Data"""

    __tablename__ = "songs"

    song_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    song_name = db.Column(db.String)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'))

    playlist = db.relationship("Playlist", back_populates="songs")


def connect_to_db(flask_app, db_uri="postgresql:///project1", echo=True):
    """Connect to the database."""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(flask_app)

    print("Connected to the database!")

if __name__ == "__main__":
    connect_to_db(app)
