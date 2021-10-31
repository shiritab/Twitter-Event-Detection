from flask import Flask
from flask_restful import Api,Resource,reqparse
import input_adapter
from functools import wraps
import  twitter_collector_basic as tw_cl



app = Flask(__name__)
api=Api(app)
Input_Adapter = input_adapter.Adapter()

# example to the use of flask server & endpoints
def home_decorator():
    def _home_decorator(f):
        @wraps(f)
        def __home_decorator(*args, **kwargs):
            # just do here everything what you need
            print('before home')
            result = f(*args, **kwargs)
            print('home result: %s' % result)
            print('after home')
            return result
        return __home_decorator
    return _home_decorator


@app.route('/router')
@home_decorator()
def home():
    return {1:1,2:2,3:4}

class Router(Resource):
    def get(self):
        Tw_Cl=tw_cl.TwitterCollector()
        Tw_Cl.read_from_twitter()
        Input_Adapter.from_twitter_to_sedtwik()
        return {"data":"this is endpoint_example"}
    def post(self):
        return {"data":"this is post endpoint_example"}

class Router1(Resource):
    def get(self):
        return {"data": "without router"}

class sedtwik(Resource):
    def get(self):
        return {"data": "without router"}
api.add_resource(Router,"/excute_sedtwik")



api.add_resource(Router1,"/")



if __name__ == '__main__':
    app.run(debug=True)