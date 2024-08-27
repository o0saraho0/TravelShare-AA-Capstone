from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    review1 = Review(
        user_id=2,
        itinerary_id=1,
        review="I wish I had seen this itinerary earlier because it would have allowed me to spend more time at these incredible places. Each location was more beautiful and interesting than I had anticipated, and I feel like I could have made the trip even more enjoyable if I had planned to stay longer at some of the spots."
    )
    review2 = Review(
        user_id=1,
        itinerary_id=4,
        review="I recently followed this itinerary, and it was an absolutely fantastic experience from start to finish. This itinerary perfectly balances relaxation and adventure, making it an ideal getaway for anyone looking to explore the beauty and culture of this region."
    )
    review3 = Review(
        user_id=5,
        itinerary_id=6,
        review="It was an unforgettable experience that I highly recommend to anyone who loves nature and scenic beauty. Despite being a short trip of only two days, it was packed with stunning views and unique opportunities to witness California's landscapes come alive with vibrant colors."
    )
    review4 = Review(
        user_id=3,
        itinerary_id=1,
        review="Overall, this five-day itinerary was well-planned and provided a perfect balance of cultural exploration and natural beauty. It was a wonderful way to experience Hangzhou, and I would highly recommend it to anyone looking to immerse themselves in the charm and tranquility of this historic city."
    )
    review5 = Review(
        user_id=7,
        itinerary_id=1,
        review="While Hangzhou is undoubtedly a beautiful city, this itinerary could benefit from more variety and interactive elements to keep travelers fully engaged throughout the five days."
    )
    review6 = Review(
        user_id=6,
        itinerary_id=3,
        review="I had an amazing time following this three-day itinerary! This trip perfectly captured the vibrant energy and unique blend of modernity and tradition that Shanghai is known for. Each day was thoughtfully planned to showcase the city's iconic sites, making it an unforgettable experience."
    )
    
    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()