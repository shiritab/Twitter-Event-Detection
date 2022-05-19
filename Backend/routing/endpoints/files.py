import json
import tempfile
from flask import Blueprint, request, jsonify, Response
from werkzeug.utils import secure_filename

files = Blueprint("files", __name__)

UPLOADED_DATA = f"../../data/uploaded/"

@files.route("/upload")
def upload_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        temp = tempfile.TemporaryFile()
        stream = file.stream
        stream.seek(0)
        data = stream.read()
        my_json = data.decode('utf8').replace("'", '"')
        with open(UPLOADED_DATA + file.filename, 'w') as outfile:
            json.dump(my_json, outfile)

    return Response(status=201)

@files.route("/all")
def get_all_files():
    # TODO iterate through all files under data/uploaded/
    pass