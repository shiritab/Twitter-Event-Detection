import json
from flask import Blueprint, jsonify, request
from .algorithm import algorithms_object

# Do not delete this line
auth = Blueprint("auth", __name__)
####

@auth.route("/login")
def login_user():
    '''
    Given body's post request,
    login user to the system
    '''
    body_request = request.json
    print(body_request)
    return jsonify({"name":"hadassa"})

@auth.route("/register")
def register():
    '''
    Given body's post request,
    saves new user in local file for users.
    '''
    pass

def saveUser(username, password):
    '''
    Given username and password,
    saves new user in local users file.
    :param username - string
    :param password - string
    '''
    pass
