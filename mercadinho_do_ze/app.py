from flask import Flask

# Extesões...
from mercadinho_do_ze.extensions import configuration


# Testes...
def minimal_app():
    app = Flask(__name__)
    configuration.init_app(app)
    return app


def create_app():
    app = minimal_app()
    configuration.init_app(app)
    configuration.carregar_extensoes(app)
    return app
