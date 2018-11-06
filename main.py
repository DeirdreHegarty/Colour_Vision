# TO RUN: FLASK_APP=main.py FLASK_DEBUG=1 flask run

from flask import Flask, request, render_template, session, url_for, redirect
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, DOCUMENTS
import os

app = Flask(__name__)
app.debug = True
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
files = UploadSet('files', 
				 ['jpg','jpeg','png','doc', 'docx', 'pdf'])	
# load the configuration for the upload sets
configure_uploads(app, files) 			



@app.route("/", methods=['GET', 'POST'])
def upload():

	# set session for file results
	if "file_urls" not in session:
		session['file_urls'] = []
	
	# uploaded file urls
	file_urls = session['file_urls']

	# clear any unsubmitted files from previous attempts
	session.pop('file_urls', None)

	# file upload from Dropzone
	if request.method == 'POST':
		file_obj = request.files
			
		for f in file_obj:

			file = request.files.get(f)
			app.logger.debug(file.filename)
			
			# save the file & append file urls
			filename = files.save(file, name=file.filename)
			file_urls.append(files.url(filename))

		session['file_urls'] = file_urls	
		
	return render_template('upload.html', title='upload')


@app.route('/results')
def results():
	# redirect to home if no files
	if "file_urls" not in session or session['file_urls'] == []:
		return redirect(url_for('upload'))


	# set the file_urls and remove the session variable
	file_urls = session['file_urls']
	session.pop('file_urls', None)

	return render_template('results.html',file_urls=file_urls)

