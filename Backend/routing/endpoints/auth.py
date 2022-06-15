import json
from flask import Blueprint, jsonify, request
from .algorithm import algorithms_object
# Do not delete this line
auth = Blueprint("auth", __name__)
####


@auth.route("/login")
def login_user():
    body_request = request.json
    print(body_request)
    return jsonify({"name":"hadassa"})

@auth.route("/register")
def register():
    pass

def saveUser(username, password):
    pass