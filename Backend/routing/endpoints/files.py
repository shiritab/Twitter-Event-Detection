import json
import tempfile
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

files = Blueprint("files", __name__)

@files.route("/upload")
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        print(file.stream)
        temp = tempfile.TemporaryFile()
        stream = file.stream
        stream.seek(0)
        data = stream.read()
        print(data)

        my_json = data.decode('utf8').replace("'", '"')
        print(my_json)
        print('- ' * 20)

        # Load the JSON to a Python list & dump it back out as formatted JSON
        data = json.loads(my_json)
        s = json.dumps(data, indent=4, sort_keys=True)
        with open('testttttttttt.json', 'w') as outfile:
            json.dump(my_json, outfile)
        with open('testttttttttt.json') as json_file:
            data = json.load(json_file)
            print(data)  # with open(file) as f:
        #
        # file.save(os.path.join('/',filename),500)
        a = "uploaded"

    return jsonify([{"hey": "hadassa"}])