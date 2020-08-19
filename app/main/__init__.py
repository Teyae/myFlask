from flask import Blueprint

self = Blueprint('main', __name__)

from app.main import views


