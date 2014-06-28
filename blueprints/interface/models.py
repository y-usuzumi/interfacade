__author__ = 'kj'

from utils.ifmodels import IFModel


class User(IFModel):
    __clct_name__ = 'user'
    __fields__ = ['username', 'password', 'email']


class Stub(IFModel):
    __clct_name__ = 'stub'
    __fields__ = ['type', 'created_by', 'time', 'comments', 'status']


class ClassStub(Stub):
    __initials__ = {'type': 'class'}
    __fields__ = ['name', 'inherited_from', 'metaclass', 'package', 'module']


class FunctionStub(Stub):
    __initials__ = {'type': 'function'}
    __fields__ = ['name', 'returns', 'parameters', 'scope']
