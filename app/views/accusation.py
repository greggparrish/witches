from app import app
from app.models.accusation import Accusation
from flask import Blueprint, render_template

accusation = Blueprint('accusation', __name__)

@accusation.route('/')
def index(page=1):
    aa = Accusation.query.order_by(Accusation.case_common_name)
    return render_template('accusation/index.html', aa=aa)

@accusation.route('/<accusation_id>')
def show(accusation_id):
    a = Accusation.query.get(accusation_id)
    return render_template('accusation/show.html', a=a)
