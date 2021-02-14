from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class NewsIngester(Resource):
  def get(self):
    return {'Hello': 'world'}
    
api add_resource(NewsIngester,'\')

if __name__ == '__main__':
  app run(debug = True)