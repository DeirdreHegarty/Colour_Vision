# Colour_Vision

#### Getting Started

*create python 3 virtual env*
```bash

# synthax
python3 -m venv <path to directory>

# venv called `.venv` in current directory
python3 -m venv .venv

# activate virtual env
source .venv/bin/activate

```

*install required dependencies*
```bash

pip3 install flask
pip3 install flask_dropzone 
pip3 install flask_uploads
pip3 install pyocr
pip3 install wand
pip3 install tesserocr
pip3 install pytesseract
pip3 install pillow
pip3 install opencv-python
pip3 install fpdf

# currently installed in virtual env
Click (7.0)
Flask (1.0.2)
Flask-Dropzone (1.5.3)
Flask-Uploads (0.2.1)
itsdangerous (1.1.0)
Jinja2 (2.10)
MarkupSafe (1.1.0)
pip (9.0.3)
setuptools (39.0.1)
Werkzeug (0.14.1)

```

*install tesseract on Mac (using brew):*
```bash

brew install imagemagick@6
ln -s /usr/local/Cellar/imagemagick@6/6.9.10-14/lib/libMagickWand-6.Q16.6.dylib  /usr/local/lib/libMagickWand.dylib

xcode-select --install
brew install tesseract --all-languages

brew install ghostscript

```


*To Run (python 3.7.1)*

#### Terminal ####
```bash

python run.py 

```
#### IPython #### 
(recommend using IPython --pdb)
```python 
run run
```
or
```python 
run run.py
```
