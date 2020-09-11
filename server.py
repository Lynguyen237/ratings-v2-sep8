"""Server for movie ratings app."""

from flask import Flask

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
"""You’ll use it to configure a Jinja2 setting to make it throw 
errors for undefined variables (by default it fails silently — 
without showing you an error message! yuck!)"""


app = Flask(__name__)

# Now let’s configure the Flask instance. 
# It’ll need a secret key (otherwise, flash and session won’t work); 
# we’ll also configure Jinja2 here as well:
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    "Show all movies"

    movie_list = crud.return_movies()

    return render_template('all_movies.html', all_movie=movie_list)


# The <movie_id2> is used as the argument input for movie_details function
@app.route('/movies/<movie_id2>')
def movie_details(movie_id2):
    "Show Movie detail"
    
    movie_detail = crud.get_movie_by_id(movie_id2)

    # 'movie' on the left is the variable in the .html5
    # This will be dynamically changed based on the movie_detail information returned
    # by the function get_movie_by_id in the crud file
    return render_template('movie_details.html', movie=movie_detail)


@app.route('/users')
def user_info():
    "Show user emails and link to their profiles"
    
    user_list = crud.return_users()

    return render_template('All_users.html', all_users=user_list)


# Part 4
@app.route('/users', methods=['POST'])
def check_user():
    """Create a new user and first check if an account already exists"""
    
    new_email = request.form.get('email') #'email' is the field name in the form on homepage.html
    new_password = request.form.get('password')

    new_user = crud.get_user_by_email(new_email)
    
    if new_user is None:
        crud.create_user(new_email, new_password)
        flash('Congrats! You can login now.')
    else:
        flash('This email already exists. Try again')

    return redirect('/')




if __name__ == '__main__':
    # Lastly, connect to your database before app.run gets called. 
    # If you don’t do this, Flask won’t be able to access your database!
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
