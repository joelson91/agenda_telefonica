from app import db


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=True)
