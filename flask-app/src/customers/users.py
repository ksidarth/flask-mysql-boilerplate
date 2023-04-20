from flask import Blueprint, request, jsonify, make_response
import json
from src import db

users = Blueprint('users', __name__)


# Get all customers from the DB
@users.route('/Users', methods=['GET'])
def get_customers():
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
@users.route('/Users/<username>', methods=['GET'])
def get_customer(username):
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
@users.route('/resident', methods=['POST'])
def post_user():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # get the request data as a dictionary
    data = request.get_json()

    username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID =\
    data["username"], data["first_name"], data["last_name"], data["email"], data["bio"], data["password"], data["dateAvailabletoBeginSublet"],
    data["dateAvailabletoEndSublet"], data["age"], data["requestID"], data["propertyID"]

    # construct the query using the request data
    query = '''
            INSERT INTO residents (username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet,
            dateAvailabletoEndSublet, age, requestID, propertyID)
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(username, first_name, last_name, email, bio, 
            password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID)


    # execute the query with the request data
    cursor.execute(query)

    # show that change has been made
    query = "SELECT * from "

    # commit the changes to the database
    db.get_db().commit()

    # return a success messagereturn
    jsonify({'message': 'Resident created successfully'})
