from flask import Flask, render_template, request, redirect
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

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
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
            'image': 'https://picsum.photos/300/400',
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

@app.route('/list', methods=['GET', 'POST'])
def get_list():
    if request.method == 'GET':
        movies = Movie.get_all()
        return render_template('movies.html', movies=movies)

    if request.method == 'POST':
        image = request.form['image']
        title = request.form['title']
        release_year = request.form['release_year']
        duration = request.form['duration']
        genre = request.form['genre']
        description = request.form['description']
        
        # check movie is not in the list
        if db.session.query(Movie).filter(Movie.title == title).count() == 0:
            data = Movie(image, title, release_year, duration, genre, description)
            movies = Movie.save(data)
                
            return render_template('movies.html', movies=movies)
        # temp 
        return render_template('layout.html')

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['movie_id']
        Movie.delete(id)        
        return redirect('/list')
        
    # temp 
    return render_template('layout.html')    

if __name__ == '__main__':
    # pass on app object to the SQLAlchemy object db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()