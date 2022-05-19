import json
import ssl

from flask import Flask
from flask_cors import CORS
from werkzeug import serving


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = "helloworld"
    CORS(app, supports_credentials=True)
    # with open("../")
    # import endpoints files
    from Backend.routing.endpoints.events import events
    from Backend.routing.endpoints.algorithm import algorithm

    # register endpoints
    app.register_blueprint(events, url_prefix="/events/")
    app.register_blueprint(algorithm, url_prefix="/algorithm/")

    return app


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
    # app.run(debug=True,port=443,host='0.0.0.0',ssl_context='adhoc')

    # app.run(debug=True,host='localhost',port=8080)
    # app.run(debug=True,host='0.0.0.0',port=443,ssl_context='adhoc')
    # with open(f'C:/Users/user/Documents/GitHub/Twitter-Event-Detection/Backend/data/tagged_tweets/tagged_tweets_dir/tagged_tweets.json', 'r') as f:
    #     data = json.load(f)
    app.run(debug=True)
    # app.run(debug=True, port=443, host='0.0.0.0', ssl_context="adhoc")
