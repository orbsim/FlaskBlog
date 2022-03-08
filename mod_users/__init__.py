from flask import Blueprint, Flask

users = Blueprint('users', __name__, url_prefix='/users/')

from .models import User
#from .views import register
from . import views