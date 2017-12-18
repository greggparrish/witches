from app import app
from app.models.accused import Accused
from flask import Blueprint, render_template

accused = Blueprint('accused', __name__, url_prefix='/accused')

@accused.route('/')
def index():
    ap = Accused.query.all()
    return render_template('accused/index.html', ap=ap)

@accused.route('/<accused_id>')
def show(accused_id):
    ap = Accused.query.filter_by(id=accused_id).first()
    return render_template('accused/show.html', ap=ap)
