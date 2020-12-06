from flask import Flask, render_template, request
import os
import csv
import random
import requests
from models import db, Movie

app = Flask(__name__)

ENV = 'dev'

# configure the PostgreSQL Connection
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
else:
    app.debug = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = ''

# pass on app object to the SQLAlchemy object db
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    # randomly select a movie
    with open('netflix_titles.csv') as f:
        reader = csv.reader(f)
        row = random.choice(list(reader))

    movie = {
        'id': row[0],
        'category': row[1],
        'title': row[2],
        'director': row[3],
        'cast': row[4],
        'country': row[5],
        'date_added': row[6],
        'release_year': row[7],
        'maturity': row[8],
        'duration': row[9],
        'genre': row[10],
        'description': row[11],
        # default poster just so we see something
        'image': 'https://live.staticflickr.com/4422/36193190861_93b15edb32_z.jpg',
        'imdb': 'Not Available'
   }

    # fetch cover image
    # call OMDB database
    OMDB_API_KEY = os.getenv('OMDB_API_KEY')
    url = f"http://www.omdbapi.com/?t={movie['title']}/&apikey={OMDB_API_KEY}"
    # get back the response
    response = requests.request("GET", url)
    # parse result into JSON and look for matching data if available
    movie_data = response.json()

    if 'Poster' in movie_data:
        movie['image'] = movie_data['Poster']
    if 'imdbRating' in movie_data:
        movie['imdb'] = movie_data['imdbRating']
    # send movie data to the movie.html template
    return render_template("movie.html", movie=movie)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        release_year = request.form['release_year']
        duration = request.form['duration']
        genre = request.form['genre']
        description = request.form['description']
        
        print(title, release_year, duration, genre, description)

        if db.session.query(Movie).filter(Movie.title == title).count() == 0:
            data = Movie(title, release_year, duration, genre, description)
            db.session.add(data)
            db.session.commit()
        
            return render_template('movies.html')
        # temp 
        return render_template('layout.html')

if __name__ == '__main__':
    app.run()