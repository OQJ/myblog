from flask import Flask
from flask_ckeditor import CKEditor
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.py')
ck = CKEditor(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"




from app import views
from app import model
from app import commands

@login_manager.user_loader
def load_user(userid):
    return model.Admin.query.get(int(userid))
