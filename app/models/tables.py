from app import db
from flask_table import Table, Col, LinkCol

class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class locado(db.Model):
    __tablename__ = "alocadas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    cpf = db.Column(db.String, unique=True)
    telcont = db.Column(db.Text, unique=True)
    telcont_pais = db.Column(db.Text)
    data_al = db.Column(db.String)


    def __init__(self, nome="", cpf="", telcont="", telcont_pais="", data_al=""):
        self.nome = nome
        self.cpf = cpf
        self.telcont = telcont
        self.telcont_pais = telcont_pais
        self.data_al = data_al

    def __repr__(self):
        return """| Nome: {} |
                  | CPF: {}  |
                  | Telefone de contato: {} |
                  | Telefone de contato dos Pais: {} |
                  | Data da alugação: {} |"""  .format(self.nome, self.cpf, self.telcont, self.telcont_pais, self.data_al)





class Results(Table):
    id = Col('Id', show=False)
    nome = Col('Nome')
    cpf = Col('Cpf')
    telcont = Col('Telefone de contato')
    telcont_pais = Col('Telefone Pais')
    data_al = Col('Data')
    edicao = LinkCol('Editar', 'edicao', url_kwargs=dict(id='id'))
    deletar = LinkCol('Deletar', 'deletar', url_kwargs=dict(id='id'))
