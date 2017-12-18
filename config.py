import os

class Config(object):
    SECRET_KEY = os.environ.get('WITCHES_SECRET')

    """ DB SETTINGS """
    WITCHES_DB = {
            'user': os.environ.get('WITCHES_USER'),
            'pass': os.environ.get('WITCHES_PASS'),
            'db': os.environ.get('WITCHES_DB'),
            }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pass)s@localhost:5432/%(db)s' % WITCHES_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestConfig(Config):
    TESTING = True
