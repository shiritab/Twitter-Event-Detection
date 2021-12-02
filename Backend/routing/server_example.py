from flask import Flask,jsonify
from flask_restful import Api,Resource,reqparse
from Backend.utils_backend import  input_adapter,sedwik_main,twitter_collector_basic as tw_cl
from functools import wraps
from flask_cors import CORS


app = Flask(__name__)
api=Api(app)
Input_Adapter = input_adapter.Adapter()
CORS(app, supports_credentials=True)

# example to the use of flask server & endpoints

class Router(Resource):
    def get(self):
        Tw_Cl=tw_cl.TwitterCollector()
        Tw_Cl.read_from_twitter()
        Input_Adapter.from_twitter_to_sedtwik()
        sedwik_main.mainFunc()

        return {"data":"this is endpoint_example"}
    def post(self):
        return {"data":"this is post endpoint_example"}

class events(Resource):
    def get(selfs):
        return jsonify({"events": [{
            "date": "2021-11-11",
            "event_name": "Bibi lose elections",
            "event_description": "during the last elections Benjanim Netanyahu lost to Naftalie Bennet",
            "tweets": [
                {
                    "Id": "264563843",
                    "text": "Evarybody knows the Sorlaks are the best",
                    "url": "www.twitter.com"
                }
            ]
        }]})
class sedtwik(Resource):
    def get(self):
        return {"data": "without router"}

api.add_resource(Router,"/excute_sedtwik")

api.add_resource(events,"/events/summary")

if __name__ == '__main__':
    app.run(debug=True)