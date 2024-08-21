from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    itinerary_id = IntegerField("Itinerary Id", validators=[DataRequired()])
    review = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")
