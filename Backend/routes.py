from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hello world'

@app.route('/Event', methods=['GET', 'POST'])
def event():
    return 'all events'

@app.route('/Event/<string:event_id>', methods=['GET'])
def eventById(event_id):
    return 'specific event following id is ' + event_id

if __name__ == '__main__':
    app.run()