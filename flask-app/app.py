# 02-SimpleRoutes Example

# import the Flask framework
from flask import Flask

# create a flask object
user = Flask(__name__)


# Defining a new handler function for the route `GET /`.
# The default method (verb) is GET, so you don't have to
# explicitly include it as I have done here.
@user.route("/", methods=['GET'])
def hello_world():
    return "<h1>Subletting Database Base route</h1>"


# this route will handle the user going to /bigHello
# It returns a different string and with the H1 html tag
# Note, without the methods parameter, it is assumed to be
# a GET route.
@user.route("/Users")
def big_hello_world():
    return "<h1>A Big Hello to you!!!!</h1>"


# Route handler for GET /users/<idNumber>
# idNumber is a variable in the URL / endpoint.
# we can access the variable in the function handler using
# curly braces.
@user.route("/users/<pets>")
def handle_user_with_id(pets):
    return f'<h2>You asked for {pets} id.'


# If this file is being run directly, then run the application
# via the app object. 
# debug = True will provide helpful debugging information and
#   allow hot reloading of the source code as you make edits and
#   save the files.
# port = 4000 binds this to network port 4000
if __name__ == '__main__':
    user.run(debug=True, port=4000)
