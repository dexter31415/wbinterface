# TODO: In your controller.py, you can import the Xelera code and invoke it through a Flask route

from flask import Blueprint, jsonify
from scripts.xelera import run_xelera_function

api = Blueprint('api', __name__)

@api.route('/run_xelera')
def run_xelera():
    result = run_xelera_function()  # This function runs Xelera code
    return jsonify({"result": result})
