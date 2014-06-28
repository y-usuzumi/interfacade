__author__ = 'kj'

from flask import Blueprint
from .controllers import index
import os

home = Blueprint('home', __name__, template_folder="templates")

@home.context_processor
def menu_action():
    return {'action': 'home'}

home.add_url_rule('/', view_func=index)
