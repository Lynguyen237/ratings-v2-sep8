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

    movies2 = crud.return_movies()

    return render_template('all_movies.html', movies=movies2)

if __name__ == '__main__':
    # Lastly, connect to your database before app.run gets called. 
    # If you don’t do this, Flask won’t be able to access your database!
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
