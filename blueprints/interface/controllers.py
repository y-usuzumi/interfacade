__author__ = 'kj'

from flask.views import View, MethodView
from flask import g, render_template, jsonify
from bson.objectid import ObjectId
from .models import *
from database import mongo
from utils.ifcodegen import IFCodeGen


class IFInterfaceView:
    def __init__(self):
        g.nav1 = 'interface'
        super().__init__()


class IndexView(MethodView, IFInterfaceView):
    def __init__(self):
        g.nav2 = 'index'
        super().__init__()

    def get(self):
        stubs = list(Stub.query.find())
        return render_template('interface/index.html', stubs=stubs)


class DetailView(MethodView, IFInterfaceView):
    def get(self, id):
        stub = Stub.query.find_one({"_id": ObjectId(id)})
        return render_template('interface/detail.html', stub=stub)


class ModulesView(MethodView, IFInterfaceView):
    def __init__(self):
        g.nav2 = 'modules'
        super().__init__()

    def get(self):
        return render_template('interface/modules.html')

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class ClassesView(MethodView, IFInterfaceView):
    def __init__(self):
        g.nav2 = 'classes'
        super().__init__()

    def get(self):
        return render_template('interface/classes.html')


class FunctionsView(MethodView, IFInterfaceView):
    def __init__(self):
        g.nav2 = 'functions'
        super().__init__()

    def get(self):
        return render_template('interface/functions.html')


class GenerateCodeView(MethodView, IFInterfaceView):
    def get(self):
        return "NIMABI"


class GenerateCodeView(MethodView):
    def get(self, id):
        stub = ClassStub(**Stub.query.find_one({'_id': ObjectId(id)}))
        res = IFCodeGen.gen(stub)
        return jsonify({'title': 'Result', 'body': res})