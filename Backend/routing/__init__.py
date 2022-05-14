from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = "helloworld"
    CORS(app, supports_credentials=True)

    # import endpoints files
    from Backend.routing.endpoints.events import events
    from Backend.routing.endpoints.algorithm import algorithm

    # register endpoints
    app.register_blueprint(events, url_prefix="/events/")
    app.register_blueprint(algorithm, url_prefix="/algorithm/")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)