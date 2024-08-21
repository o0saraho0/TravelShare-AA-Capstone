from .db import db, environment, SCHEMA, add_prefix_for_prod

class Itinerary(db.Model):
    __tablename__ = "itineraries"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    preview_image_url = db.Column(db.Text, nullable=False)
    traveler_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("categories.id")))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    category = db.relationship("Category", back_populates="itinerary")
    traveler = db.relationship("User", back_populates="itinerary")
    schedule = db.relationship('Schedule', back_populates='itinerary', cascade="all, delete-orphan")
    review = db.relationship('Review', back_populates='itinerary', cascade="all, delete-orphan")
    collection = db.relationship('Collection', back_populates='itinerary')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "country": self.country,
            "description": self.description,
            "preview_image_url": self.preview_image_url,
            "traveler": self.traveler.to_dict(),
            "category_id": self.category_id,
            "schedules": [el.to_dict() for el in self.schedule]
        }
    

class Schedule(db.Model):
    __tablename__ = "schedules"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String, nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("itineraries.id")))
    
    itinerary = db.relationship("Itinerary", back_populates="schedule")
    activity = db.relationship('Activity', back_populates='schedule', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "day": self.day,
            "itinerary_id": self.itinerary_id,
            "activities": [el.to_dict() for el in self.activity]
        }
    

class Activity(db.Model):
    __tablename__ = "activities"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    place_image_url = db.Column(db.Text)
    schedule_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("schedules.id")))
    
    schedule = db.relationship("Schedule", back_populates="activity")

    def to_dict(self):
        return {
            "id": self.id,
            "place": self.place,
            "description": self.description,
            "place_image_url": self.place_image_url,
            "schedule_id": self.schedule_id
        }
    

class Category(db.Model):
    __tablename__ = "categories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)

    itinerary = db.relationship("Itinerary", back_populates="category")


    def to_dict(self):
        return {
            "id": self.id, 
            "type": self.type
        }


    
    

