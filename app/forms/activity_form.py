from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ActivityForm(FlaskForm):
    place = StringField("Place", validators=[DataRequired()])
    longitude= FloatField("Longitude", validators=[DataRequired()])
    latitude= FloatField("Latitude", validators=[DataRequired()])
    description = TextAreaField("Description")
    place_image_url = TextAreaField("Place Image")
    schedule_id = IntegerField("Schedule Id", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Submit")