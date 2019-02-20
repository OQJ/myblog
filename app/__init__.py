from flask import Flask
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config.from_pyfile('config.py')
ck = CKEditor(app)




from app import views
from app import model
from app import commands