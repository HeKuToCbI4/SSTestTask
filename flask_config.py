import os

import config_data as cfgd

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Spooky scary skeletons'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{cfgd.pg_user}:{cfgd.pg_pwd}@{cfgd.vm_ip}:{cfgd.postgres_port}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False


class StageConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
