import json
import ssl

from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug import serving

# Todo edit-Niv
def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = "helloworld"
    CORS(app, supports_credentials=True)
    # with open("../")
    # import endpoints files
    from Backend.routing.endpoints.events import events
    from Backend.routing.endpoints.algorithm import algorithm
    from Backend.routing.endpoints.files import files
    from Backend.routing.endpoints.auth import auth


    # register endpoints
    app.register_blueprint(events, url_prefix="/events/")
    app.register_blueprint(algorithm, url_prefix="/algorithm/")
    app.register_blueprint(files, url_prefix="/files/")
    app.register_blueprint(auth, url_prefix="/auth/")



    return app

import json
import tempfile
from flask import Blueprint, request
from werkzeug.utils import secure_filename

files = Blueprint("files", __name__)



# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# serving.run_simple( '0.0.0.0',443, app, ssl_context="adhoc")

#
# @app.route("/")
# def main():
# #     # print(requests.get("https://web-development-environments-2021.github.io/312359359/").text)
#     print("in req")
#     return  " niv from server "
#
# if __name__ == '__main__':
#     app.run(debug=True,port=443,host='0.0.0.0',ssl_context="adhoc")

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    app = create_app()
    # serving.run_simple( host='0.0.0.0',pory=443, application=app, ssl_context=context)
    # app.run(debug=True,port=443,host='localhost')

    # app.run(debug=True,host='localhost',port=8080)
    # app.run(debug=True,host='0.0.0.0',port=443,ssl_context='adhoc')
    # with open(f'C:/Users/user/Documents/GitHub/Twitter-Event-Detection/Backend/data/tagged_tweets/tagged_tweets_dir/tagged_tweets.json', 'r') as f:
    #     data = json.load(f)
    # app.run(debug=True)
    # app.run(debug=True, port=443, host='localhost')

    # for https connection
    app.run(debug=True, port=443, host='0.0.0.0', ssl_context="adhoc")

