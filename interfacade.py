from flask import Flask, render_template
from database import mongo

class IFApp(Flask):
    pass

app = IFApp(__name__)
app.config.from_pyfile('config.py')

mongo.init_app(app)

from blueprints import interface, home
app.register_blueprint(interface, url_prefix='/interface')
app.register_blueprint(home, url_prefix='/')


def seed_database():
    from blueprints.interface.models import User, Stub, ClassStub, FunctionStub
    from time import time
    with app.app_context():
        mongo.db.drop_collection(User.__clct_name__)
        mongo.db.drop_collection(Stub.__clct_name__)
        u = User(username='kennethb',
                 password='kennethb',
                 email='newelevenken@aliyun.com')
        clsstub = ClassStub(created_by='kj',
                            time=time(),
                            name='test_class',
                            inherited_from='e',
                            metaclass='IFModel',
                            package='interfacade.utils',
                            module='models')
        funcstub = FunctionStub(created_by='kj',
                                time=time(),
                                name='test_func',
                                returns='int',
                                parameters=['a', 'b'],
                                scope='test_class')
        User.query.insert(u)
        Stub.query.insert(clsstub)
        Stub.query.insert(funcstub)


if __name__ == '__main__':
    import os

    seed_database()
    app.run()
