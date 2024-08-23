from flask import Blueprint, request, session
from flask_login import current_user, login_required
from ..models import db
from ..models.itinerary import Activity
from ..forms import ActivityForm


activities_routes = Blueprint("activities", __name__)

# Get all activities by scheduleId
@activities_routes.route("/schedule/<int:scheduleId>", methods=["GET"])
def activities_by_scheduleId(scheduleId):
    activities = Activity.query.filter(Activity.schedule_id == scheduleId).all()
    return [activity.to_dict() for activity in activities], 200

# Create activity
@activities_routes.route("/schedule/<int:scheduleId>/new", methods=["POST"])
@login_required
def add_activity(scheduleId):
    form = ActivityForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        newActivity = Activity(
            place=form.place.data,
            longitude=form.longitude.data,
            latitude=form.latitude.data,
            description=form.description.data,
            place_image_url=form.place_image_url.data,
            schedule_id=scheduleId
        )
        db.session.add(newActivity)
        db.session.commit()
        return newActivity.to_dict(), 201
    else:
        print("Form errors:", form.errors)
        return form.errors, 400
    
# Delete activity by activity id
@activities_routes.route("/<int:activityId>", methods=["DELETE"])
@login_required
def delete_activity(activityId):
    activity = Activity.query.filter(Activity.id == activityId).one()

    if activity is None:
        return {"error": "Activity could not be found"}, 404

    db.session.delete(activity)
    db.session.commit()

    return {"message": "Successfully deleted"}, 200


# Edit activity by activity id
@activities_routes.route("/<int:activityId>/edit", methods=["PUT"])
@login_required
def edit_activity(activityId):
    form = ActivityForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        activity = Activity.query.get(activityId)
        if activity:
            activity.place=form.data["place"]
            activity.longitude=form.data["longitude"]
            activity.latitude=form.data["latitude"]
            activity.description=form.data["description"]
            activity.place_image_url=form.data["place_image_url"]
        db.session.commit()
        return activity.to_dict(), 200
    else:
        print("Form errors:", form.errors)
        return form.errors, 400