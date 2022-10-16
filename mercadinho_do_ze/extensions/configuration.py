from importlib import import_module
from dynaconf import FlaskDynaconf


def carregar_extensoes(app):
    for extensoes in app.config.get('EXTENSIONS'):
        modulo = import_module(extensoes)
        modulo.init_app(app)


def init_app(app):
    FlaskDynaconf(app)
