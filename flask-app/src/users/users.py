from flask import Blueprint, request, jsonify, make_response, current_app
import json
from flaskext.mysql import MySQL

db = MySQL()
users = Blueprint('users', __name__)


# Get all users from the DB
@users.route('/', methods=['GET'])
def get_users():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT id, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, propertyID FROM resident')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


# Get user detail for user with particular username
@users.route('/users/<username>', methods=['GET'])
def get_user(username):
    cursor = db.get_db().cursor()
    cursor.execute('select * from USER where username = {0}'.format(username))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Adds a new User to the database
@users.route('/user', methods=['POST'])
def post_user():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # get the request data as a dictionary
    data = request.get_json()

    username, first_name, last_name, email, bio, age, password, dateJoined, dateBeginSublet, dateEndSublet, pets, password, zipcode, requestID =\
    data["username"], data["first_name"], data["last_name"], data["email"], data["bio"], data["age"], data["password"],
    data["dateJoined"], data["dateBeginSublet"], data["dateEndSublet"], data["pets"], data["password"], data["zipcode"], data["requestID"]

    # construct the query using the request data
    query = '''
            INSERT INTO user (username, first_name, last_name, email, bio, age, password, dateJoined, dateBeginSublet
            dateEndSublet, pets, password, zipcode, requestID)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(username, 
            first_name, last_name, email, bio, age, password, dateJoined, dateBeginSublet, dateEndSublet, pets, password, zipcode, requestID)


    # execute the query with the request data
    cursor.execute(query)

    # show that change has been made
    query = 'SELECT * from where username="' + str(username) + '"'

    # commit the changes to the database
    db.get_db().commit()

    # return a success message
    jsonify({'message': 'Resident created successfully'})

# add a subletRequest
@users.route('/subletRequests', methods=['POST'])
def add_request():
    the_data = request.json
    current_app.logger.info(the_data)

    id = the_data['id']
    isResolved = the_data['isResolved']
    dateResolved = the_data['dateResolved']
    info = the_data['info']
    dateSubmitted = the_data['dateSubmitted']
    residentUsername = the_data['residentUsername']

    cursor = db.get_db().cursor()
    cursor.execute('insert into subletRequest(id, isResolved, dateResolved, info, dateSubmitted, residentUsername) values ("{0}", "{1}", {2}, {3}, {4})'
                   .format(id, isResolved, dateResolved, info, dateSubmitted, residentUsername))
    db.get_db().commit()
    response = (jsonify(the_data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

# Change the date their sublet ends
@users.route('<username>/dateEndSublet', methods=['PUT'])
def change_date(username):
    the_data = request.json
    current_app.logger.info(the_data)

    date = the_data['dateEndSublet']
    query = '''
        UPDATE user
        SET dateEndSublet = '{}'
        WHERE username = '{}'
    '''.format(date, username)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'


# Removes a User
@users.route('/user/<id>', methods=['DELETE'])
def remove_user(username):
    query = '''
        DELETE FROM users
        WHERE username = '{}' '''.format(username)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

# get all current subletRequests
@users.route('/user', methods=['GET'])
def get_songs():
    cursor = db.get_db().cursor()
    query = '''
        SELECT DISTINCT info 
        FROM subletRequest
        WHERE info IS NOT NULL
    '''
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Change a users bio based off its username
@users.route('<username>/bio', methods=['PUT'])
def edit_bio(username):
    the_data = request.json
    current_app.logger.info(the_data)

    bio = the_data['bio']
    query = '''
        UPDATE user
        SET bio = '{}'
        WHERE username = '{}'
    '''.format(bio, username)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'