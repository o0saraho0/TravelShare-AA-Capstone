from .db import db, environment, SCHEMA, add_prefix_for_prod

class Collection(db.Model):
    __tablename__ = "collections"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('itineraries.id')), nullable=False)

    itinerary = db.relationship('Itinerary', back_populates='collection')
    user = db.relationship('User', back_populates='collection')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "itinerary_id": self.itinerary_id
        }