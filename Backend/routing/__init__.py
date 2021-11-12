from flask import Flask
from flask_cors import CORS
from os import name, path


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = "helloworld"
    CORS(app, supports_credentials=True)

    from events import events

    app.register_blueprint(events, url_prefix="/events/")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    