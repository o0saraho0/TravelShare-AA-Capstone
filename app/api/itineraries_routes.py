from flask import Blueprint, request, session
from flask_login import current_user, login_required
from ..models import db
from ..models.itinerary import Itinerary, Schedule
# from ..models.user import User
# from sqlalchemy.exc import SQLAlchemyError
from ..forms import ItineraryForm


itineraries_routes = Blueprint("itineraries", __name__)

# Get all itineraries owned by current user
@itineraries_routes.route("/current", methods=["GET"])
@login_required
def itineraries_manage():
    itineraries = Itinerary.query.filter(Itinerary.traveler_id == current_user.id).all()
    return [itinerary.to_dict() for itinerary in itineraries], 200

# Delete itinerary by itinerary id
@itineraries_routes.route("/<int:itineraryId>", methods=["DELETE"])
@login_required
def delete_itinerary(itineraryId):
    itinerary = Itinerary.query.filter(Itinerary.id == itineraryId).one()

    if itinerary is None:
        return {"error": "Itinerary could not be found"}, 404

    db.session.delete(itinerary)
    db.session.commit()

    return {"message": "Successfully deleted"}, 200

# Edit itinerary by itinerary id
@itineraries_routes.route("/<int:itineraryId>/edit", methods=["PUT"])
@login_required
def edit_itinerary(itineraryId):
    form = ItineraryForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        itinerary = Itinerary.query.get(itineraryId)
        if itinerary:
            original_duration = itinerary.duration
            itinerary.title=form.data["title"]
            itinerary.duration=form.data["duration"]
            itinerary.description=form.data["description"]
            itinerary.preview_image_url=form.data["preview_image_url"]
            itinerary.category_id=form.data["category_id"]

            if original_duration != itinerary.duration:
                current_schedules = Schedule.query.filter_by(itinerary_id=itinerary.id).all()

                if itinerary.duration > original_duration:
                    for day_number in range(original_duration + 1, itinerary.duration + 1):
                        new_schedule = Schedule(
                            day=f"Day {day_number}",
                            itinerary_id=itinerary.id
                        )
                        db.session.add(new_schedule)

                elif itinerary.duration < original_duration:
                    schedules_to_delete = [
                        schedule for schedule in current_schedules
                        if int(schedule.day.split()[-1]) > itinerary.duration
                    ]
                    for schedule in schedules_to_delete:
                        db.session.delete(schedule)

        db.session.commit()
        return itinerary.to_dict(), 200
    else:
        print("Form errors:", form.errors)
        return form.errors, 400

# Create a new itinerary
@itineraries_routes.route("/new", methods=["POST"])
@login_required
def create_itinerary():
    form = ItineraryForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        newItinerary = Itinerary(
            title=form.title.data,
            duration=form.duration.data,
            description=form.description.data,
            preview_image_url=form.preview_image_url.data,
            category_id=form.category_id.data,
            traveler_id=current_user.id
        )
        db.session.add(newItinerary)
        db.session.commit()

        # Create schedules based on the duration
        for day_number in range(1, newItinerary.duration + 1):
            new_schedule = Schedule(
                day=f"Day {day_number}",
                itinerary_id=newItinerary.id
            )
            db.session.add(new_schedule)
        
        db.session.commit()
        return newItinerary.to_dict(), 201
    else:
        print("Form errors:", form.errors)
        return form.errors, 400
        

# Get itinerary by itinerary id
@itineraries_routes.route("/<int:itineraryId>", methods=["GET"])
def itinerary_by_id(itineraryId):
    itinerary = Itinerary.query.filter(Itinerary.id == itineraryId).one()

    if itinerary is None:
        return {"message": "Itinerary could not be found"}, 404

    return itinerary.to_dict(), 200

# Get all itineraries
@itineraries_routes.route("/", methods=["GET"])
def get_all_itineraries():
    itineraries = Itinerary.query.all()
    return [itinerary.to_dict() for itinerary in itineraries], 200