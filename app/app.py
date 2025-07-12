
#import os
#import sys


#sys.path.insert(0, os.path.dirname(__file__))


#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/plain')])
#    message = 'It works!\n'
#    version = 'Python %s\n' % sys.version.split()[0]
#    response = '\n'.join([message, version])
#    return [response.encode()]


import os
import sys
from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS
import importlib
import json

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# --- Production-like route ---
@app.route('/viru')
def doviru():
    return render_template('viru.html')

@app.route('/')
def production_check():
    """
    This route provides a simple "It works!" message along with the Python version,
    similar to your production code.
    """
    message = 'It works! and works wonderfully\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return response, 200, {'Content-Type': 'text/plain'}

# --- Development route ---
@app.route('/pf', methods=['GET', 'POST'])
def dataService():
    """
    This route is from your development code and currently returns a simple greeting.
    You can expand this function to handle more complex logic.
    """
    print("entered adminService")
    return "hi how r u"

if __name__ == '__main__':
    # This part is typically used for development to run the Flask server directly.
    # For production, you would usually use a WSGI server like Gunicorn or uWSGI.
    app.run(debug=True)
