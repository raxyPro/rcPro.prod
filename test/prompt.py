# passenger_wsgi.py
#test 1223

import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the create_app function from app package
from app import create_app

# Create the WSGI application object
application = create_app()

#ap.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# app/__init__.py

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    @app.route('/do1')
    def do1():
        return 'hi, World!'

    @app.route('/do2')
    def do2():
        return 'hi, World!'

    @app.route('/env')
    def show_env():
        import os
        env_info = [f"{k} = {v}" for k, v in os.environ.items()]
        return "<br>".join(env_info)    

    return app
