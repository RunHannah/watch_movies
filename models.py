from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500))
    title = db.Column(db.String(200))
    release_year = db.Column(db.String(4))
    duration = db.Column(db.String(200))
    genre = db.Column(db.String(200))
    description = db.Column(db.Text())

    # constructor
    def __init__(self, image, title, release_year, duration, genre, description):
        self.image = image
        self.title = title
        self.release_year = release_year
        self.duration = duration
        self.genre = genre
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Movie.query.all()
        