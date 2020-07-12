# app/catalog/__init__.py

# Blueprints are a set operations that can be registered for applications
# They help build a structure for large apps
from flask import Blueprint
authentication = Blueprint('authentication', __name__, template_folder='templates')

from app.auth import routes