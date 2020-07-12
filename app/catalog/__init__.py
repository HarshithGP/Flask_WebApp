# app/catalog/__init__.py

# Blueprints are a set operations that can be registered for applications
# They help build a structure for large apps
from flask import Blueprint
main = Blueprint('main', __name__, template_folder='templates')

from app.catalog import routes