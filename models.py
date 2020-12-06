from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    release_year = db.Column(db.String(4))
    duration = db.Column(db.String(200))
    genre = db.Column(db.String(200))
    description = db.Column(db.Text())

    # constructor
    def __init__(self, title, release_year, duration, genre, description):
        self.title = title
        self.release_year = release_year
        self.duration = duration
        self.genre = genre
        self.description = description
