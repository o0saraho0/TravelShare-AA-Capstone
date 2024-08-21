from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('itineraries.id')), nullable=False)
    review = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    user = db.relationship('User', back_populates='review')
    itinerary = db.relationship('Itinerary', back_populates='review')

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "itinerary_id": self.itinerary_id,
            "review": self.review,
            "updated_at": self.updated_at
        }
