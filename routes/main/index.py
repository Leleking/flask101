from flask import Blueprint, jsonify
index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def welcome():
    return jsonify({'data': 'welcome to the main'})
