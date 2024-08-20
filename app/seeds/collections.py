from app.models import db, Collection, environment, SCHEMA
from sqlalchemy.sql import text


def seed_collections():
    collection1 = Collection(
        user_id=1,
        itinerary_id=2,
    )
    collection2 = Collection(
        user_id=1,
        itinerary_id=6,
    )
    
    db.session.add(collection1)
    db.session.add(collection2)

    db.session.commit()


def undo_collections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collections"))
        
    db.session.commit()