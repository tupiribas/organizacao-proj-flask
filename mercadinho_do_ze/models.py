from mercadinho_do_ze.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Produtos(db.Model, SerializerMixin):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140))
    preco = db.Column(db.Numeric())


class Usuario(db.Model, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(140))
    senha = db.Column(db.String(512))
