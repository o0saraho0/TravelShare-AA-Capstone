from app.models import db, Category, environment, SCHEMA
from sqlalchemy.sql import text

# Adds demo categories
def seed_categories():
    category1 = Category(type="City Exploration")
    category2 = Category(type="Nature Escapes")
    category3 = Category(type="Road Trips")
    
    db.session.add(category1)
    db.session.add(category2)
    db.session.add(category3)
    db.session.commit()


def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM categories"))
        
    db.session.commit()