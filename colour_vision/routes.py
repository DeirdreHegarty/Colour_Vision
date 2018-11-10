from flask import Flask, request, render_template, session, url_for, redirect, send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES, DOCUMENTS
from colour_vision import app
import os.path
from colour_vision.extract_text import retrieveTextFromImage



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
			print(file)
			app.logger.debug(file.filename)
			
			# save the file & append file urls
			filename = files.save(file, name=file.filename)
			file_urls.append(files.url(filename))
			session['filename']=filename

			#config(file.filename)

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
	print(file_urls)
	config_thing(session['filename'])
	
	return render_template('results.html',file_urls=file_urls , file_path = 'Output.txt')

@app.route('/results/<path:filename>')
def download_file(filename):
	import time
	time.sleep(5)
	return send_from_directory(directory="./../downloads", filename=filename, as_attachment=True)
	 

def f_type(filename):
	"""returns the file type, for example .png, .pdf ... etc
	
	Arguments:
		filename {str} -- full file name something.ext
	"""	
	ext = os.path.splitext(filename)[1]
	return ext

def config_thing(filename):
	"""given some configuration, apply to file
	"""
	if f_type(filename) == ".jpg":
		text = retrieveTextFromImage(os.getcwd()+"/uploads/"+filename)
		text_file = open(os.getcwd()+"/downloads/"+"Output.txt", "w")
		text_file.write(text)
		text_file.close()
		# return send_from_directory(directory="./", filename='extract_text.py', as_attachment=True)
		# download_file(filename)

