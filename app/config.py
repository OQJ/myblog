import os
import sys

from app import app


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')


SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'HAHAHAHAHAH'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
CKEDITOR_HEIGHT = 300
