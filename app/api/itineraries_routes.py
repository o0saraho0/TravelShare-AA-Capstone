from flask import Blueprint, request, session, jsonify
from flask_login import current_user, login_required
from ..models import db
from ..models.itinerary import Itinerary, Schedule, Activity, Category
from ..models.user import User
from sqlalchemy.exc import SQLAlchemyError
import random


itineraries_routes = Blueprint("itineraries", __name__)

# Get all itineraries owned by current user
@itineraries_routes.route("/current", methods=["GET"])
def itineraries_manage():
    itineraries = Itinerary.query.filter(Itinerary.traveler_id == current_user.id).all()
    return [itinerary.to_dict() for itinerary in itineraries], 200

# Delete itinerary by itinerary id
@itineraries_routes.route("/<int:itineraryId>", methods=["DELETE"])
def delete_itinerary(itineraryId):
    itinerary = Itinerary.query.filter(Itinerary.id == itineraryId).one()

    if itinerary is None:
        return {"error": "Itinerary could not be found"}, 404

    db.session.delete(itinerary)
    db.session.commit()

    return {"message": "Successfully deleted"}, 200

# Edit itinerary by itinerary id

# Create a new itinerary

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