from flask import Blueprint, request, session, jsonify
from flask_login import current_user, login_required
from ..models import db
from ..models.collection import Collection

collections_routes = Blueprint("collections", __name__)

@collections_routes.route("/current")
@login_required
def get_collections():
    collections = Collection.query.filter(Collection.user_id == current_user.id).all()
    print(collections)

    return [collection.to_dict() for collection in collections]


@collections_routes.route("/<int:itineraryId>", methods=['DELETE'])
@login_required
def remove_collections(itineraryId):
    preFav = Collection.query.filter(Collection.itinerary_id == itineraryId).filter(Collection.user_id == current_user.id).first()

    if preFav: 
        db.session.delete(preFav)
        db.session.commit()
        return {"id": preFav.id, "user_id": current_user.id}, 200
    
    return { "message": "Collection could not be found."}, 404 


@collections_routes.route("/<int:itineraryId>", methods=['POST'])
@login_required
def add_collection(itineraryId):
    preFav = Collection.query.filter(Collection.itinerary_id == itineraryId).filter(Collection.user_id == current_user.id).first()

    if not preFav:
        new_collection = Collection(
        user_id=current_user.id,
        itinerary_id=itineraryId,
        )
        db.session.add(new_collection)
        db.session.commit()
        return new_collection.to_dict(), 200
    
    return { "message": "User already collected this itinerary."}, 500 
