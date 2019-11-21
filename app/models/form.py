from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class CreateForm(FlaskForm):

    nome = StringField("nome", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    telcont = StringField("telcont", validators=[DataRequired()])
    telcont_pais = StringField("telcont_pais", validators=[DataRequired()])
    data_al = StringField("data_al", validators=[DataRequired()])

class UpdateForm(FlaskForm):
    nome_search = StringField("nome_search")
