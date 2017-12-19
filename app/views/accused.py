from app import app
from app.models.accused import Accused, AccusedFamily
from flask import Blueprint, render_template
from nvd3 import pieChart

accused = Blueprint('accused', __name__)

@accused.route('/')
def index():
    ap = Accused.query.order_by(Accused.last_name).limit(20)
    return render_template('accused/index.html', ap=ap)

@accused.route('/<accused_id>')
def show(accused_id):
    ap = Accused.query.filter_by(id=accused_id).first()
    return render_template('accused/show.html', ap=ap)

