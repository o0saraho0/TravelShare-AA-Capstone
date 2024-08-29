from flask import Blueprint, request
from app.models import db, Itinerary, Activity
from ..forms.image_form import PreviewImageForm, PlaceImageForm
from flask_login import current_user, login_required
from .s3_helpers import (
    upload_file_to_s3, get_unique_filename, remove_file_from_s3, ALLOWED_EXTENSIONS)

images_routes = Blueprint("images", __name__)


# create itinerary image


@images_routes.route("/itineraries/new", methods=["POST"])
@login_required
def upload_preview_image():
    form = PreviewImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        image = request.files["preview_image_url"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        if "url" not in upload:
            # If there's an error in upload, return it
            return {"message": "Failed to upload image in backend"}, 400

        # Return the image URL
        url = upload["url"]
        return {"preview_image_url": url}, 200

    return {"Form errors": form.errors}, 400


# update itinerary image


@images_routes.route("/itineraries/<int:itineraryId>", methods=["PUT"])
@login_required
def edit_preview_image(itineraryId):
    form = PreviewImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        itinerary = Itinerary.query.get(itineraryId)

        if itinerary is None:
            return {"message": "Itinerary not found"}, 404

        if itinerary.traveler_id != current_user.id:
            return {"message": "You do not have permission to edit this itinerary"}, 403

        # Get the new image file
        image = request.files["preview_image_url"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        if "url" not in upload:
            return {"message": "Failed to upload image in backend"}, 400

        # Optionally remove the old image from S3
        if itinerary.preview_image_url:
            remove_file_from_s3(itinerary.preview_image_url)

        # Update the itinerary with the new image URL
        url = upload["url"]
        return {"preview_image_url": url}, 200

    return {"Form errors": form.errors}, 400


# create activity image


@images_routes.route("/activities/new", methods=["POST"])
@login_required
def upload_activity_image():
    form = PlaceImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        image = request.files["place_image_url"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        if "url" not in upload:
            # If there's an error in upload, return it
            return {"message": "Failed to upload image in backend"}, 400

        # Return the image URL
        url = upload["url"]
        return {"place_image_url": url}, 200

    return {"Form errors": form.errors}, 400


# update activity image


@images_routes.route("/activities/<int:activityId>", methods=["PUT"])
@login_required
def edit_activity_image(activityId):
    form = PlaceImageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        activity = Activity.query.get(activityId)

        if activity is None:
            return {"message": "Activity not found"}, 404

        # Get the new image file
        image = request.files["place_image_url"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        if "url" not in upload:
            return {"message": "Failed to upload image in backend"}, 400

        # Optionally remove the old image from S3
        if activity.place_image_url:
            remove_file_from_s3(activity.place_image_url)

        # Update the itinerary with the new image URL
        url = upload["url"]
        return {"place_image_url": url}, 200

    return {"Form errors": form.errors}, 400
