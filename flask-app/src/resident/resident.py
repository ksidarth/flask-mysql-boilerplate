from flask import Blueprint, request, jsonify, make_response
import json
from src import db

resident = Blueprint('resident', __name__)


# Get all the residents from the database
@resident.route('/resident', methods=['GET'])
def get_resident():
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

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@resident.route('/resident', methods=['POST'])
def post_resident():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # get the request data as a dictionary
    data = request.get_json()

    # construct the query using the request data
    query = '''
            INSERT INTO residents (username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet,
            dateAvailabletoEndSublet, age, requestID, propertyID)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
    # execute the query with the request data
    cursor.execute(query, (data['username'], data['first_name'], data['last_name'],
                          data['email'], data['bio'], data['password'],
                          data['dateAvailabletoBeginSublet'], data['dateAvailabletoEndSublet'], data['age'],
                          data['requestID'], data['propertyID']))

    # commit the changes to the database
    db.get_db().commit()

    # return a success messagereturn 
    jsonify({'message': 'Resident created successfully'})

@resident.route('/resident', methods=['PUT'])
def put_resident():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of residents
    cursor.execute('SELECT username, first_name, last_name, email, bio, password, dateAvailabletoBeginSublet, dateAvailabletoEndSublet, age, requestID, propertyID FROM residents')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify({'message': 'Resident updated successfully'})


@resident.route('/resident', methods=['DELETE'])
def delete_resident():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # extract the ID of the resident to delete from the request
    resident_id = request.args.get('id')

    # use cursor to delete the resident from the database
    cursor.execute('DELETE FROM residents WHERE id = %s', (resident_id,))

    # commit the changes to the database
    db.get_db().commit()

    return jsonify({'message': 'Resident deletedx successfully'})
