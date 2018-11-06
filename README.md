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

*to run in debug mode*
```bash

cd Colour_Vision
FLASK_APP=main.py FLASK_DEBUG=1 flask run

```
