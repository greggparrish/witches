import logging
import os

from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

""" INIT APP """
app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

""" INIT UTILS """
db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)

""" VIEWS """
from app.views.static import static
from app.views.accused import accused
from app.views.trial import trial
app.register_blueprint(accused)
app.register_blueprint(static)
app.register_blueprint(trial)

""" ASSETS """
assets = Environment(app)
assets.url = app.static_url_path
js = Bundle(
        'js/base.js',
        filters='rjsmin',
        output='public/js/witches.js')
css = Bundle(
        'scss/application.scss',
        filters='pyscss',
        output='public/css/style.css',
        depends='scss/partials/*.scss')
assets.register('js_all', js)
assets.register('css_all', css)
