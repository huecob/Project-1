"""Create, Read, Update, Delete"""

from model import db, User, Playlist, Song, Weather
from app import app

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def find_user_by_email(email):
    """Quieries our DB for a user"""

    return User.query.filter(User.email == email).first()