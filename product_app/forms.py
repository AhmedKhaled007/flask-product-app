from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    color = SelectField("color", validators=[DataRequired()])
    size = SelectField("Size", validators=[DataRequired()])
    price = DecimalField("Price", validators=[
                         DataRequired(), NumberRange(min=0)], widget=NumberInput(step="0.01", min="0"))
    submit = SubmitField('Create Product')
