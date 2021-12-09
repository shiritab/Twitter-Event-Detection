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

import pandas as pd


df=pd.read_csv(r"C:\Users\meiri\Desktop\חומרים לימודיים\שנה ג\Downloads\relevant_tweets.tsv", sep='\t')
df.to_csv('results_csv', index=False,float_format='%.16f')
# print(df.iloc[:,1].values)
class Router(Resource):
    def get(self):
        Tw_Cl=tw_cl.TwitterCollector()
        Tw_Cl.read_from_twitter()
        Input_Adapter.from_twitter_to_sedtwik()
        # sedwik_main.mainFunc()

        return {"data":"this is endpoint_example"}
    def post(self):
        return {"data":"this is post endpoint_example"}

class events(Resource):
    def get(selfs):
        return jsonify(sedwik_main.mainFunc())

class sedtwik(Resource):
    def get(self):
        return {"data": "without router"}

api.add_resource(Router,"/excute_sedtwik")

api.add_resource(events,"/events/summary")

if __name__ == '__main__':
    app.run(debug=True)