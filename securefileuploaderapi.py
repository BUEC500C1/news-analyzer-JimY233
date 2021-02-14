from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class SecureFileUploader(Resource):
  def get(self):
    return {'Hello': 'world'}
    
api.add_resource(SecureFileUploader,'/')

if __name__ == '__main__':
  app run(debug = True)
