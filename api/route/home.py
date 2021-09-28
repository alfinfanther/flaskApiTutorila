from flask import Blueprint
from flask import jsonify

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return jsonify({'message':'hello world'})
