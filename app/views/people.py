from app import app
from app.models.people import Accused, AccusedFamily
from flask import Blueprint, render_template
from nvd3 import pieChart

people = Blueprint('people', __name__)

@people.route('/')
def accused_index():
    ap = Accused.query.order_by(Accused.last_name).limit(20)
    return render_template('people/accused_index.html', ap=ap)

@people.route('/<accused_id>')
def accused_show(accused_id):
    ap = Accused.query.get(accused_id)
    return render_template('people/accused_show.html', ap=ap)
