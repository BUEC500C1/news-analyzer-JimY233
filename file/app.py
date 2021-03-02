import flask
from flask import render_template
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request, redirect

from werkzeug.utils import secure_filename

import logging
import sqlite3
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/user/Downloads/'

@app.route('/')
def home():
   return render_template('upload.html')
	
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(file.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
  app.run(debug = True)
