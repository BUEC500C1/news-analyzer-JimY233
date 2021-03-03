"""
NLP analysis
Procedure-based Api
"""
from flask import Flask
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

#data in json file for example
TEXT = {"TEXT_ID": "text_id",
               "TEXT": "text",
               "Sentiment": "semtiment",
               "NLP": ["nlp1","nlp2","nlp3"]
              }    

'''
Events
Event_Convert: File is converted to text in English  
Event_Process: NLP analysis request and process the analysis 
Event_Update: File is updated and re-analyze again
'''

def convert_text():
  "convert the input to text in English"
  pass
  
def create_data():
  '''
  check if it is text and in English, if not, use convert_text()
  if convert event not successful, log error message
  return success or failure
  '''
  pass

def update_data(data,message):
  '''
  update the data with requirement and log the message
  return success or failure
  '''
  pass

def delete_data(data):
  '''
  delete the data and log the message
  return success or failure
  '''
  pass


class NLPanalysis(Resource):
  def post(self): #create: upload file and create the data for this file
    '''
    if Event_upload:
      create_data() #create data
    '''
    return {'Hello': 'world'}
  def delete(self): #delete: delete the file and relating data
    pass
  def put(self): #update: update the data record
    pass
  def get(self): #read: read data json file and return information
    pass
    
api.add_resource(NLPanalysis,'/')

if __name__ == '__main__':
  app.run(debug = True)
