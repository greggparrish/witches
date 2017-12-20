from app import app
from app.models.trial import Trial
from flask import Blueprint, render_template

trial = Blueprint('trial', __name__)

@trial.route('/')
def index(page=1):
    tt = Trial.query.order_by(Trial.case_common_name)
    return render_template('trial/index.html', tt=tt)

@trial.route('/<trial_id>')
def show(trial_id):
    t = Trial.query.get(trial_id)
    return render_template('trial/show.html', t=t)

