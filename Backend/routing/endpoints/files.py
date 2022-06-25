import json
import tempfile
from flask import Blueprint, request, jsonify, Response
from werkzeug.utils import secure_filename
import markdown

# Do not delete these lines
files = Blueprint("files", __name__)

UPLOADED_DATA = f"../../data/uploaded/"
##

@files.route("/upload")
def upload_file():
    '''
    Given file object via body's post request,
    saves it under UPLOADED_DATA local path.
    '''
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
    '''
    Iterates through all files under UPLOADED_DATA
    '''
    pass

@files.route("/markdown")
def get_markdown():
    '''
    Returns markdown file as html string
    '''
    with open("./../../README.md", 'r') as readme_file:
        return str(markdown.markdown(readme_file.read()))
