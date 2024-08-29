from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.s3_helpers import ALLOWED_EXTENSIONS


class PreviewImageForm(FlaskForm):
    preview_image_url = FileField("Preview Image File", validators=[
        FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])


class PlaceImageForm(FlaskForm):
    place_image_url = FileField("Place Image File", validators=[
        FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
