import ssl
from flask import Flask, jsonify
from flask_cors import CORS
# import endpoints files
from Backend.routing.endpoints.events import events
from Backend.routing.endpoints.algorithm import algorithm
from Backend.routing.endpoints.files import files
from Backend.routing.endpoints.auth import auth
from flask import Blueprint, request

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    # register endpoints
    app.register_blueprint(events, url_prefix="/events/")
    app.register_blueprint(algorithm, url_prefix="/algorithm/")
    app.register_blueprint(files, url_prefix="/files/")
    app.register_blueprint(auth, url_prefix="/auth/")
    return app

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    app = create_app()
    # for https connection
    app.run(debug=True, port=443, host='0.0.0.0',ssl_context="adhoc")

