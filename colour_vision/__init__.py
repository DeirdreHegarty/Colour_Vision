# TO RUN: FLASK_APP=main.py FLASK_DEBUG=1 flask run

from flask import Flask, request, render_template, session, url_for, redirect
from flask_dropzone import Dropzone

import os

app = Flask(__name__)
dropzone = Dropzone(app)

# DROPZONE SETTINGS
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf, .doc, .txt'
app.config['DROPZONE_INVALID_FILE_TYPE']
app.config['DROPZONE_REDIRECT_VIEW'] = 'results' 	# redirect to results.html
app.config['DROPZONE_MAX_FILE_SIZE'] = 10
app.config['SECRET_KEY'] = 'secretkey'

# UPLOADS SETTINGS
app.config['UPLOADED_FILES_DEST'] = os.getcwd() + '/uploads'
# name of upload set, allowed extensions

from colour_vision import routes


