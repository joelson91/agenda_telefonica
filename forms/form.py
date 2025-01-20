from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SubmitField


class UserForm(FlaskForm):
    nome = StringField("Nome")
    telefone = TelField("Telefone")
    email = EmailField("Email")
    btn_submit = SubmitField("Salvar")