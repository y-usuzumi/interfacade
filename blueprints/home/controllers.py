__author__ = 'kj'

from flask.views import View, MethodView
from flask import g, render_template

def index():
    g.nav1 = 'home'
    return render_template('home/index.html')