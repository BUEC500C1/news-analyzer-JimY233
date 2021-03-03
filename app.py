import flask
from flask import render_template
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request, redirect

from werkzeug.utils import secure_filename
import PyPDF2

import logging
import sqlite3
import os

from nlp.nlp_search import *

app = Flask(__name__)

#where pdf files saved
app.config['UPLOAD_FOLDER'] = 'C:/Users/user/Downloads/'

@app.route('/')
def home():
   return render_template('upload.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       if 'username' in request.form and 'password' in request.form:
          return "do_the_login()"
    else:
        return "show_the_login_form()"
	
@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      f.save(path)
      logging.info("PDF temporarily saved")

      page_content = ""
      pdfFileObj = open(path, 'rb') 
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
      totalpage = pdfReader.numPages
      logging.info("Number of pages:",totalpage)
      for page in range(totalpage): 
         pageObject = pdfReader.getPage(page) 
         page_content = page_content + pageObject.extractText()
      logging.info("PDF converted to text")

      #os.remove(path)
      #logging.info("PDF deleted")

      #database insert
      conn = sqlite3.connect('mydatabase.db')
      cursor = conn.cursor ()
      cursor.execute('create table if not exists files (id, text)') 
      id = 0  
      cursor.execute('insert into files values(?,?)',(id,page_content))
      cursor.close()  
      conn.commit()   
      conn.close()

      #database search
      conn = sqlite3.connect('mydatabase.db')
      cursor = conn.cursor()
      cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
      Tables=cursor.fetchall()
      logging.info("Tables in the databse:",Tables)
      cursor.execute('select text from files where id=?', (0,))
      values = cursor.fetchall()
      #print(type(values)) #values in class list
      freq = search_nlp("Discussion",values)
      print(freq) #keyword freq search
      cursor.close()
      conn.close()

      pdfFileObj.close()  

      return 'file uploaded successfully'

if __name__ == '__main__':
  app.run(debug = True)
