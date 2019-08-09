from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# DO NOT REMOVE !1111
# Required for migrations...
from pg_provider import pg_models

app = Flask(__name__)
app.config.from_object('flask_config.StageConfig')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
