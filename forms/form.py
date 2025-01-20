from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    telefone = TelField("Telefone", validators=[DataRequired()])
    email = EmailField("Email")
    btn_submit = SubmitField("Salvar")