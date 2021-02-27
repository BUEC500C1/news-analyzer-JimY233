"""
Secure File Uploader/Ingester
Entity-based Api
"""
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#file record in json file for example
files = {
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
tasks = {
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

"""
'''
Events
Event_upload: Upload the file
Event_convert: Convert the file to text
Event_modify: File content is modified
'''
def create_data():
  '''
  if upload event not successful, log error message
  if part of information missing, log missing part name
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


class SecureFileUploader(Resource):
  def post(self): #create: upload file and create the data for this file
    '''
    if Event_upload:
      create_data() #create file_record
    '''
    return {'Hello': 'world'}
  def delete(self): #delete: delete the file and relating file_record
    pass
  def put(self): #update: update the file_record
    pass
  def get(self): #read: read data json file and return information
    pass
    
api.add_resource(SecureFileUploader,'/')
"""

@app.route('/todo/api/v1.0/file', methods=['GET'])
def get_files():
    return jsonify({'files': files})

@app.route('/todo/api/v1.0/files/<string:file_id>', methods=['GET'])
def get_file(file_id):
    file = filter(lambda t: t['id'] == file_id, files)
    if len(files) == 0:
        abort(404)
    return jsonify({'file': files[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<string:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
  app.run(debug = True)
