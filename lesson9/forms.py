from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrar')

# StringField: Campo de texto
# PasswordField: Campo de Senha
# SubmitField: Botão de envio
# validators: Regras para validar o que o usuario digitou
