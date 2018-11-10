from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import cv2
import os
import pytesseract
from fpdf import FPDF

def retrieveTextFromPDF(PDF_in):

	tool = pyocr.get_available_tools()[0]
	lang = tool.get_available_languages()[0] # english language

	req_image = []
	final_text = []

	# convert .PDF tp jpeg
	image_pdf = Image(filename=PDF_in, resolution=300)
	image_jpeg = image_pdf.convert('jpeg')

	# wand has converted all the separate pages in the PDF into separate image blobs
	# which OCR is then run over
	for img in image_jpeg.sequence:
		img_page = Image(image=img)
		req_image.append(img_page.make_blob('jpeg'))

	for img in req_image: 
		txt = tool.image_to_string(
			PI.open(io.BytesIO(img)),
			lang=lang,
			builder=pyocr.builders.TextBuilder()
		)
		final_text.append(txt)

	return txt

def retrieveTextFromImage(image_in):
	print(image_in)
	# load the example image and convert it to grayscale
	image = cv2.imread(image_in)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	 
	# threshold image
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
	# gray = cv2.medianBlur(gray, 3)
	 
	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	text = pytesseract.image_to_string(PI.open(filename))
	os.remove(filename)

	return text

def convertToPDF(text_in):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font('Arial', 'B', 16)
	pdf.cell(40, 10, text_in)
	pdf.output('tuto1.pdf', 'F')







