from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

resident = Blueprint('resident', __name__)

def execute_command(command):
    cursor = db.get_db().cursor()
    cursor.execute(command)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    return json_data


def json_response(json_data):
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# get all resident
@resident.route('/', methods=['GET'])
def get_resident():
    json_data_resident = execute_command('select * from resident')
    for resident in json_data_resident:
        json_data_resident = execute_command('select * from user WHERE username="{0}"'.format(resident['username']))
        resident.update(json_data_resident[0])
    return json_response(json_data_resident)


# get all resident
@resident.route('/resident', methods=['GET'])
def get_resident():
    return json_response(execute_command('select * from resident'))


# add a resident
@resident.route('/resident', methods=['POST'])
def post_resident():
    the_data = request.json
    current_app.logger.info(the_data)

    username = the_data['username']
    first_name = the_data['first_name']
    last_name = the_data['last_name']
    email = the_data['email']
    bio = the_data['bio']
    password = the_data[password]
    dateAvailabletoBeginSublet = the_data[dateAvailabletoBeginSublet]
    dateAvailabletoEndSublet = the_data[dateAvailabletoEndSublet]
    age = the_data[age]
    requestID = the_data[requestID]
    propertyID = the_data[propertyID]

    cursor = db.get_db().cursor()
    cursor.execute('insert into review (username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID) values ("{0}", "{1}", {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'
                   .format(username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID))
    db.get_db().commit()
    json_data_review = execute_command('select * from review WHERE review_id={0}'.format(cursor.lastrowid))
    return json_response(json_data_review)


# get a resident based on username
@resident.route('/<username>', methods=['GET'])
def get_resident(username):
    json_data_reviewer = execute_command('select * from resident WHERE username="{0}"'.format(username))[0]
    json_data_reviewer.update(execute_command('select * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_data_reviewer)


# update a resident's biography
@resident.route('/<username>/bio', methods=['PUT'])
def put_bio(username):
    the_data = request.json
    current_app.logger.info(the_data)

    bio = the_data['bio']

    cursor = db.get_db().cursor()
    cursor.execute('update user set biography="{0}" WHERE username="{1}"'.format(bio, username))
    db.get_db().commit()
    json_data_reviewer = execute_command('select * from reviewer WHERE username="{0}"'.format(username))[0]
    json_data_reviewer.update(execute_command('select * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_data_reviewer)

# delete a resident based on resident username
@resident.route('/resident/<id>', methods=['DELETE'])
def delete_resident(username):

    cursor = db.get_db().cursor()
    cursor.execute('delete from resident WHERE resident={0}'.format(username))
    db.get_db().commit()
    return json_response({'message': 'resident successfully deleted'})

# get a resident's email based on username
@resident.route('/<username>/email', methods=['GET'])
def get_email(username):
    json_data_reviewer = execute_command('select email from resident WHERE username="{0}"'.format(username))[0]
    return json_response(json_data_reviewer)


# update a resident's email
@resident.route('/<username>/email', methods=['PUT'])
def put_email(username):
    the_data = request.json
    current_app.logger.info(the_data)

    email = the_data['email']

    cursor = db.get_db().cursor()
    cursor.execute('update user set email="{0}" WHERE username="{1}"'.format(email, username))
    db.get_db().commit()
    json_data_reviewer = execute_command('select * from reviewer WHERE username="{0}"'.format(username))[0]
    json_data_reviewer.update(execute_command('select * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_data_reviewer)

#update a resident's dateAvailabletoBeginSublet

@resident.route('/<username>/dateAvailabletoBeginSublet', methods=['PUT'])
def put_bio(username):
    the_data = request.json
    current_app.logger.info(the_data)

    dateAvailabletoBeginSublet = the_data['dateAvailabletoBeginSublet']

    cursor = db.get_db().cursor()
    cursor.execute('update user dateAvailabletoBeginSublet="{0}" WHERE username="{1}"'.format(dateAvailabletoBeginSublet, username))
    db.get_db().commit()
    json_data_reviewer = execute_command('select * from reviewer WHERE username="{0}"'.format(username))[0]
    json_data_reviewer.update(execute_command('select * from subletRequest WHERE username="{0}"'.format(username))[0])
    return json_response(json_data_reviewer)

    