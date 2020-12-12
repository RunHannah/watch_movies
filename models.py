from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)
    image = db.Column(db.String(500))
    title = db.Column(db.String(200))
    release_year = db.Column(db.String(4))
    duration = db.Column(db.String(200))
    genre = db.Column(db.String(200))
    description = db.Column(db.Text())

    # constructor
    def __init__(self, movie_id, image, title, release_year, duration, genre, description):
        self.movie_id = movie_id
        self.image = image
        self.title = title
        self.release_year = release_year
        self.duration = duration
        self.genre = genre
        self.description = description

    def save(data):
        db.session.add(data)
        db.session.commit()
 
        movies_list = Movie.get_all()
        results = []
        for movie in movies_list:
            obj = {
                'id': movie.id,
                'movie_id': movie.movie_id,
                'image': movie.image,
                'title': movie.title,
                'release_year': movie.release_year,
                'duration': movie.duration,
                'genre': movie.genre,
                'description': movie.description
            }
            results.append(obj)
        return results

    @staticmethod
    def get_all():
        return Movie.query.all()
    
    def delete(id):
        movie = Movie.query.filter(Movie.movie_id == id).first()
        db.session.delete(movie)
        db.session.commit()