"""Data model for App :)"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User Information"""

    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}"
    
class Playlist(db.Model):
    """Playlist Stuff"""

    __tablename__ = "Playlists"

    playlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    playlist_name = db.Column(db.String)
    playlist_weather = db.Column(db.Integer)

    weather = db.relationship("Weathers", back_populates="playlist")
    songs = db.relationship("Songs", back_populates="playlist")

class Songs(db.Model):
    """Music Data"""

    __tablename__ = "Songs"

    song_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    song_name = db.Column(db.String)

class Weather(db.Model):
    """Weather data"""

    __tablename__ = "Weathers"

    weather_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    weather_type = db.Column(db.String)
    

if __name__ == "__main__":

    from server import app
    connect_to_db(app)