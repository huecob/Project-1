from model import db, User, Playlist, Song, Weather
from server import app

def seed_data():
    # Create users
    user1 = User(email='user1@example.com', password='password1')
    user2 = User(email='user2@example.com', password='password2')

    # Create weather data
    sunny_weather = Weather(weather_type='sunny')
    rainy_weather = Weather(weather_type='rainy')

    # Create playlists
    playlist1 = Playlist(playlist_name='Sunny Day Playlist', weather=sunny_weather)
    playlist2 = Playlist(playlist_name='Rainy Day Playlist', weather=rainy_weather)

    # Create songs
    song1 = Song(song_name='Song 1', playlist=playlist1)
    song2 = Song(song_name='Song 2', playlist=playlist1)
    song3 = Song(song_name='Song 3', playlist=playlist2)
    song4 = Song(song_name='Song 4', playlist=playlist2)

    # Add objects to session and commit to database
    with app.app_context():
        db.create_all()
        db.session.add_all([user1, user2, sunny_weather, rainy_weather, playlist1, playlist2, song1, song2, song3, song4])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("success!")
