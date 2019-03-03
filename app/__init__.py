from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config.from_object(Config)
heroku = Heroku(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors