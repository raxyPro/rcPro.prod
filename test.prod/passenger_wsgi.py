import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the create_app function from app package
from app import create_app

# Create the WSGI application object
application = create_app()