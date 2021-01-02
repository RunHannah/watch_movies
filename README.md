# RandoFlix

RandoFlix generates a random movie or show suggestion based on Netflix content as of 2019.
A user can create a list, add or remove an item from the list, or watch the content by clicking a button that links out to Netflix's site (some content may no longer be available).

![Farmers Market Finder Demo](demo/demo.gif)

#### Technologies Used

```
Application: Python, Flask, JavaScript, HTML, CSS, Bootstrap
Database: PostgreSQL, SQLAlchemy
Data Source: www.kaggle.com/shivamb/netflix-shows

Note this project was built using Python 3.9.0 and Postgres 13.1, and requires Postgres installed on your machine.
```

## 🚀 Quick start

1.  **Create an account on Kaggle.com and download csv data set**

    ```shell
    https://www.kaggle.com/shivamb/netflix-shows
    ```

2.  **Clone Repo**

    ```shell
    $ git clone https://github.com/RunHannah/watch_movies.git
    ```

3.  **Navigate to Directory**

    ```shell
    $ cd watch_movies/
    ```

4.  **Unzip csv data file and add netflix_shows.csv file at root directory**

5.  **Create .env file at root directory**

6.  **Obtain an API Key from OMDB at www.omdbapi.com/, and add to .env file using the following format:**
    ```shell
    export OMDB_API_KEY="OMDB_API_KEY_HERE"
    ```
7.  **Start PostgreSQL server and create a database called netflix_movies**

    ```shell
    pg_ctl -D /usr/local/var/postgres start
    psql postgres

    ```

8.  **Add to .env file the following info with your username and password for the netflix_movies database**

```shell
export DATABASE_URL="postgresql://<username>:<password>@localhost/netflix_movies"
```

9.  **Activate virtual environment and install dependencies**

```shell
$ pipenv shell
$ pipenv install
```

10. **Start the development mode**

```shell
$ python app.py
```

Site is now running at `http://127.0.0.1:5000/`

## License

This project is licensed under the MIT License

```

```
