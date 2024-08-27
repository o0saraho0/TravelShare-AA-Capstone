from flask import Blueprint, request, session, jsonify
from flask_login import current_user, login_required
from ..models import db
from ..models.review import Review
from ..forms import ReviewForm
from sqlalchemy.exc import SQLAlchemyError

comments_routes = Blueprint("comments", __name__)

@comments_routes.route("/itineraries/<int:itineraryId>")
def get_collections(itineraryId):
    comments = Review.query.filter(Review.itinerary_id == itineraryId).all()

    return [comment.to_dict() for comment in comments]


@comments_routes.route("/<int:commentId>", methods=['DELETE'])
@login_required
def delete_comment(commentId):
    preComment = Review.query.filter(Review.id == commentId).one()

    if not current_user.id == preComment.user_id:
        return { "message": "Unauthorized." }, 401

    if preComment: 
        db.session.delete(preComment)
        db.session.commit()
        return {"id": preComment.id, "user_id": current_user.id}, 200
    
    return { "message": "Comment could not be found."}, 404 


@comments_routes.route("/itineraries/<int:itineraryId>/new", methods=['POST'])
@login_required
def add_comment(itineraryId):
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        new_comment = Review(
            user_id=current_user.id,
            itinerary_id=itineraryId,
            review=form.review.data,
        )
        print(new_comment)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment.to_dict(), 201
    else:
        print("Form errors:", form.errors)
        return form.errors, 400
    

@comments_routes.route("/<int:commentId>/edit", methods=['PUT'])
@login_required
def edit_comment(commentId):
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        comment = Review.query.filter(Review.id == commentId).first()

        if not current_user.id == comment.user_id:
            return { "message": "Unauthorized." }, 401
        
        comment.review = form.data["review"]
        db.session.commit()
        return comment.to_dict()
    else:
        print("Form errors:", form.errors)
        return form.errors, 400
