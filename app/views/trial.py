from app import app
from app.models.trial import Trial
from flask import Blueprint, render_template

trial = Blueprint('trial', __name__, url_prefix='/trials')

@trial.route('/')
def index():
    trials = Trial.query.all()
    return render_template('trial/index.html', trials=trials)

@trial.route('/<trial_id>')
def show(trial_id):
    t = Trial.query.filter_by(id=trial_id).first()
    return render_template('trial/show.html', t=t)

