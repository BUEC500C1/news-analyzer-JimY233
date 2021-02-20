"""
NewsIngester
Procedure-based Api
"""
from flask import Flask
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

#data in json file for example
data = {
    "ID:/document/User_ID/File_ID": {
        "Uploadtime": "2021.2.17",
        "FileURL": "securefileuploader/file1.pdf",
        "FileMetadata": {"Authors": ["Jiaming Yu", "jimmy", "jiamingy"],
                         "Modifiedtime": "2021.2.17",
                         "File source": "google",
                         "File size": "15MB",
                         "File tags": ["tag1","tag2","tag3"]
                        },
      "TEXT": {"TEXT_ID": "text_id",
               "TEXT": "text",
               "Sentiment": "semtiment",
               "NLP": ["nlp1","nlp2","nlp3"]
              }    
    }
}

'''
Events
Event_Searchbykeyword: searched url according to the keyword
Event_Download: Download from the web according to the url
Event_Upload: upload the news file to the dataset
'''

def search_from_web(keyword):
  '''
  search from the web to derive the url according to the keyword
  '''
  pass
  
def create_data(keyword):
  '''
  url = search_from_web(keyword)
  text = download(url)
  analyze text and upload
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


class NewsIngester(Resource):
  def post(self): #create: download news file and create the data for this file
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
    
api.add_resource(SecureFileUploader,'/')

if __name__ == '__main__':
  app.run(debug = True)
