from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ActivityForm(FlaskForm):
    place = StringField("Place", validators=[DataRequired()])
    description = TextAreaField("Description")
    place_image_url = TextAreaField("Place Image")
    schedule_id = IntegerField("Schedule Id", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Submit")