from sqlalchemy import create_engine, MetaData
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Produtos(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140))
    price = db.Column(db.Numeric())


db.create_all()
print(Produtos.__tablename__)

# Testando conecao com o banco de dados
engine = create_engine('mysql+pymysql://root:3x3Rc1t0@localhost/test')
metadata = MetaData(bind=engine)

user = engine.execute('select * from produtos').first()

print(user)
