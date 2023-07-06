rom flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class BookForm(FlaskForm):
    author = StringField('Author name', validators=[DataRequired()])
    numBooks = IntegerField('Number of books to display', validators=[DataRequired()])
    sorting = SelectField('Sorting option', validators=[DataRequired()])
    submit = SubmitField('See Books')