from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.StageConfig')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app import routes
