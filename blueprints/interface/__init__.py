__author__ = 'kj'

from flask import Blueprint
from .controllers import *

interface = Blueprint('interface', __name__, template_folder="templates")

@interface.context_processor
def menu_action():
    return {'nav1': 'interface'}

interface.add_url_rule('/', view_func=IndexView.as_view('index'))
interface.add_url_rule('/<id>', view_func=DetailView.as_view('detail'))
interface.add_url_rule('/modules', view_func=ModulesView.as_view('modules'))
interface.add_url_rule('/classes', view_func=ClassesView.as_view('classes'))
interface.add_url_rule('/functions', view_func=FunctionsView.as_view('functions'))
interface.add_url_rule('/<id>/generate_code', view_func=GenerateCodeView.as_view('generate_code'))