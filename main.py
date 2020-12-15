from flask import Flask
from flask_restful import Resource, Api
from scarp import webScrap

app = Flask(__name__)
api = Api(app)

class test(Resource):
    def get(self):
        return webScrap()

api.add_resource(test, '/')
app.run(debug=True, port=8000)
