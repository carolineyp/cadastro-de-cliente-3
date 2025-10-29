from prova import db
from datetime import datetime






class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String(100), nullable=True)
    cpf = db.Column(db.String(11), nullable=True)



