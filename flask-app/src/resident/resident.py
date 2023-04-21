from flask import Blueprint, request, jsonify, make_response, current_app
import json
from flaskext.mysql import MySQL
import db
db = MySQL()

resident = Blueprint('resident', __name__)

def execute_command(command):
    cursor = db.get_db().cursor()
    cursor.execute(command)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return json_data

def json_response(json_data):
    response = make_response(jsonify(json_data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response


# get all resident
@resident.route('/', methods=['GET'])
def get_residents():
    json_data_resident = execute_command('SELECT * from resident')
    for resident in json_data_resident:
        json_data_resident = execute_command('SELECT * from resident WHERE username="{0}"'.format(resident['username']))
        resident.update(json_data_resident[0])
    return json_response(json_data_resident)

# add a resident
@resident.route('/resident', methods=['POST'])
def post_resident():
    theData = request.json
    current_app.logger.info(theData)

    username = theData['username']
    first_name = theData['first_name']
    last_name = theData['last_name']
    email = theData['email']
    bio = theData['bio']
    password = theData[password]
    dateAvailabletoBeginSublet = theData[dateAvailabletoBeginSublet]
    dateAvailabletoEndSublet = theData[dateAvailabletoEndSublet]
    age = theData[age]
    requestID = theData[requestID]
    propertyID = theData[propertyID]

    cursor = db.get_db().cursor()
    cursor.execute('insert into resident (username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID) values ("{0}", "{1}", {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'
                   .format(username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID))
    db.get_db().commit()
    json_resident = execute_command('SELECT * from resident WHERE resident_id={0}'.format(cursor.lastrowid))
    return json_response(json_resident)


# get a resident based on username
@resident.route('/<username>', methods=['GET'])
def get_resident(username):
    json_resident = execute_command('SELECT * from resident WHERE username="{0}"'.format(username))[0]
    json_resident.update(execute_command('SELECT * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_resident)


# update a resident's bio
@resident.route('/<username>/bio', methods=['PUT'])
def put_bio(username):
    theData = request.json
    current_app.logger.info(theData)

    bio = theData['bio']

    cursor = db.get_db().cursor()
    cursor.execute('update resident biography="{0}" WHERE username="{1}"'.format(bio, username))
    db.get_db().commit()
    json_resident = execute_command('SELECT * from resident WHERE username="{0}"'.format(username))[0]
    json_resident.update(execute_command('SELECT * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_resident)

# delete a resident based on resident username
@resident.route('/resident/<id>', methods=['DELETE'])
def delete_resident(username):

    cursor = db.get_db().cursor()
    cursor.execute('delete from resident WHERE resident={0}'.format(username))
    db.get_db().commit()
    return json_response({'message': 'resident successfully deleted'})

 # get a resident's email based on username
@resident.route('/<username>', methods=['GET'])
def get_resident_emails(username):
    json_data_resident = execute_command('SELECT email from resident WHERE username="{0}"'.format(username))[0]
    json_data_resident.update(execute_command('SELECT email from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_data_resident)

# update a resident's email
@resident.route('/<username>/email', methods=['PUT'])
def put_email(username):
    theData = request.json
    current_app.logger.info(theData)

    bio = theData['bio']

    cursor = db.get_db().cursor()
    cursor.execute('update residentset biography="{0}" WHERE username="{1}"'.format(bio, username))
    db.get_db().commit()
    json_resident = execute_command('SELECT * from resident WHERE username="{0}"'.format(username))[0]
    json_resident.update(execute_command('SELECT * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_resident)

# update a resident's dateAvailabletoBeginSublet
@resident.route('/<username>/dateAvailabletoBeginSublet', methods=['PUT'])
def put_date(username):
    theData = request.json
    current_app.logger.info(theData)

    dateAvailabletoBeginSublet = theData['dateAvailabletoBeginSublet']

    cursor = db.get_db().cursor()
    cursor.execute('update residentset biography="{0}" WHERE username="{1}"'.format(dateAvailabletoBeginSublet, username))
    db.get_db().commit()
    json_resident = execute_command('SELECT * from resident WHERE username="{0}"'.format(username))[0]
    json_resident.update(execute_command('SELECT * from subletRequest WHERE username="{0}"'.format(username))[0])