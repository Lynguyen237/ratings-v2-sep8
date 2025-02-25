"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings
movies_in_db = []
for movie in movie_data:
    title = movie ['title'],
    overview = movie ['overview'],
    poster_path = movie ['poster_path'],
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title, overview, release_date, poster_path)

    movies_in_db.append(db_movie)

for n in range (10):
    email = f'user{n}@test.com' # Voila! A unique email!
    password = 'test'

    db_user = crud.create_user(email, password)

    for i in range (10):
        movie = choice(movies_in_db)
        score = randint(1,5)
        db_rating = crud.create_rating(db_user, movie, score)


# More code will go here

########################
# This code will
# Drop the database with dropdb

# Create the database with createdb

# Use db.create_all to create tables

# Automatically populate the database with data:

# Use data from data/movies.json to create movies

# Create 10 random users; for each user, create 10 ratings on random movies with random scores