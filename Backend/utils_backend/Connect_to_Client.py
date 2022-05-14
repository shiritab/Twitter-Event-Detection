import daemon as daemon
import gevent
import requests
from flask import Flask
from werkzeug import serving
import ssl

app = Flask(__name__)

# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# serving.run_simple( '0.0.0.0',443, app, ssl_context="adhoc")


@app.route("/")
def main():
#     # print(requests.get("https://web-development-environments-2021.github.io/312359359/").text)
    print("in req")
    return  "from server "

if __name__ == '__main__':
    app.run(debug=True,port=443,host='0.0.0.0',ssl_context="adhoc")