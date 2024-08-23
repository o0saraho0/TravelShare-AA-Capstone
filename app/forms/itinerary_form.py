from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ItineraryForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired(), NumberRange(min=0)])
    description = TextAreaField("Description")
    preview_image_url = TextAreaField("Preview Image", validators=[DataRequired()])
    category_id = IntegerField("Category", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Submit")