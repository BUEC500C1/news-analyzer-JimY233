import flask
from flask import Flask,render_template, request, redirect, url_for,flash,session

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

import PyPDF2
import sqlite3
import os

import logging

from nlp.nlp_search import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) 

#where pdf files saved
app.config['UPLOAD_FOLDER'] = 'C:/Users/user/Downloads/'

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      if 'username' in request.form and 'password' in request.form:
         username = request.form['username']
         password = request.form['password']

         conn = sqlite3.connect('mydatabase.db')
         cursor = conn.cursor()
         cursor.execute('create table if not exists user (username, password)') 

         error = None
         user = cursor.execute(
             'SELECT * FROM user WHERE username = ?', (username,)
         ).fetchone()
         print(user)
         if user is None:
            error = 'Incorrect username.'
         #user is tuple 0-username 1-password
         elif not check_password_hash(str(user[1]), password):
            error = 'Incorrect password.'

         if error is None:
            session.clear()
            session['user_id'] = user[0]
            return render_template('upload.html')

         cursor.close()
         conn.close()
         flash(error)
         return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      
      conn = sqlite3.connect('mydatabase.db')
      cursor = conn.cursor ()
      cursor.execute('create table if not exists user (username, password)') 
      
      error = None
      if not username:
         error = 'Username is required.'
      elif not password:
         error = 'Password is required.'
      elif cursor.execute(
         'SELECT username FROM user WHERE username = ?', (username,)
      ).fetchone() is not None:
         error = 'User {} is already registered.'.format(username)     

      if error is None:
         cursor.execute(
               'INSERT INTO user (username, password) VALUES (?, ?)',
               (username, generate_password_hash(password))
         )
         cursor.close()
         conn.commit() 
         conn.close()
         return render_template('login.html')

      cursor.close()
      conn.close()
      flash(error)
      return render_template('register.html')

	
@app.route('/upload', methods = ['GET', 'POST'])
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

      flash('file uploaded successfully')

      return render_template('upload.html')

if __name__ == '__main__':
  app.run(debug = True)
