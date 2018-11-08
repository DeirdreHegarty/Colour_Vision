from flask import Flask, request, render_template, session, url_for, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES, DOCUMENTS
from colour_vision import app

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

