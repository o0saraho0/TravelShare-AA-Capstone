from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    review1 = Review(
        user_id=2,
        itinerary_id=1,
        review="I wish I had seen this itinerary earlier because it would have allowed me to spend more time at these incredible places. Each location was more beautiful and interesting than I had anticipated, and I feel like I could have made the trip even more enjoyable if I had planned to stay longer at some of the spots."
    )
    review2 = Review(
        user_id=3,
        itinerary_id=1,
        review="Overall, this five-day itinerary was well-planned and provided a perfect balance of cultural exploration and natural beauty. It was a wonderful way to experience Hangzhou, and I would highly recommend it to anyone looking to immerse themselves in the charm and tranquility of this historic city."
    )
    review3 = Review(
        user_id=7,
        itinerary_id=1,
        review="While Hangzhou is undoubtedly a beautiful city, this itinerary could benefit from more variety and interactive elements to keep travelers fully engaged throughout the five days."
    )
    review4 = Review(
        user_id=7,
        itinerary_id=2,
        review="The '3 Days in Hangzhou' itinerary was a fantastic experience! Each day was packed with exciting activities, from the serene beauty of West Lake to the lively atmosphere of Hefang Street. The highlight was definitely the tea house visit, which provided a perfect blend of relaxation and cultural immersion. Highly recommend this itinerary for anyone visiting Hangzhou!"
    )
    review5 = Review(
        user_id=8,
        itinerary_id=2,
        review="I absolutely loved this Hangzhou itinerary! It covered all the must-see spots in just three days, making it perfect for a quick trip. The pacing was great, with a mix of sightseeing, shopping, and relaxation. The West Lake was stunning, and the tea houses offered a cozy escape from the city's hustle and bustle. A well-thought-out itinerary that I would happily follow again."
    )
    review6 = Review(
        user_id=6,
        itinerary_id=3,
        review="I had an amazing time following this three-day itinerary! This trip perfectly captured the vibrant energy and unique blend of modernity and tradition that Shanghai is known for. Each day was thoughtfully planned to showcase the city's iconic sites, making it an unforgettable experience."
    )
    review7 = Review(
        user_id=2,
        itinerary_id=4,
        review="I recently followed this itinerary, and it was an absolutely fantastic experience from start to finish. This itinerary perfectly balances relaxation and adventure, making it an ideal getaway for anyone looking to explore the beauty and culture of this region."
    )
    review8 = Review(
        user_id=5,
        itinerary_id=4,
        review="This Tulum and Cancun itinerary exceeded my expectations! Every day was packed with exciting activities, from exploring the mesmerizing Mayan ruins to snorkeling in stunning cenotes. The balance between adventure and relaxation was perfect, giving me a chance to soak up the sun on beautiful beaches while also experiencing the rich cultural heritage of the region. I highly recommend this itinerary to anyone looking for a memorable vacation!"
    )
    review9 = Review(
        user_id=5,
        itinerary_id=6,
        review="It was an unforgettable experience that I highly recommend to anyone who loves nature and scenic beauty. Despite being a short trip of only two days, it was packed with stunning views and unique opportunities to witness California's landscapes come alive with vibrant colors."
    )
    review10 = Review(
        user_id=6,
        itinerary_id=6,
        review="The California Wildflower Road Trip was a dream come true for nature lovers! The fields of colorful blooms were breathtaking, and the itinerary was well-organized, allowing us to see the best spots without feeling rushed. The Carrizo Plain was my favorite stop, with its endless vistas of wildflowers. Perfect for a quick getaway and great for photographers!"
    )
    review11 = Review(
        user_id=7,
        itinerary_id=6,
        review="I was a bit disappointed with the California Wildflower Road Trip. While the flowers were beautiful, the timing of the trip didn't quite match the peak bloom period, so many areas were sparse. Also, the itinerary felt a bit rushed, leaving little time to fully enjoy each location. I wish there had been more information about the best time to visit for maximum bloom."
    )
    review12 = Review(
        user_id=2,
        itinerary_id=7,
        review="The Pacific Coast Highway Road Trip was absolutely spectacular! The views along the route were breathtaking, especially through Big Sur, where the cliffs meet the ocean. Each stop along the way, from Monterey's charming streets to Malibu's sandy beaches, added its own unique charm. The itinerary was well-paced, allowing plenty of time to soak in the sights and explore. A must-do for anyone looking to experience California's coastline at its finest!"
    )
    review13 = Review(
        user_id=7,
        itinerary_id=8,
        review="The Hawaii Family Vacation itinerary was perfect for our family! We loved the variety of activities, from hiking Diamond Head to relaxing on the stunning beaches. The kids enjoyed the visit to Pearl Harbor, which was both educational and moving. Every day was well-planned, allowing us to experience the beauty and culture of Hawaii without feeling rushed. Highly recommend this for families looking for a mix of adventure and relaxation!"
    )
    review14 = Review(
        user_id=8,
        itinerary_id=8,
        review="What a fantastic family trip! The 'Hawaii Family Vacation' itinerary provided the perfect balance of sightseeing and downtime. We loved snorkeling in Hanauma Bay and exploring the lush gardens. The accommodations were family-friendly, and the activities kept everyone engaged, from our youngest to the teens. This trip created wonderful memories for our family, and we can't wait to return!"
    )
    review15 = Review(
        user_id=2,
        itinerary_id=9,
        review="The Pittsburgh Cultural and Scenic Trip was a fantastic experience! Each day was well planned and filled with iconic sites like the Duquesne Incline and the Cathedral of Learning. The itinerary beautifully combined Pittsburgh's rich history with its vibrant culture. We especially enjoyed the breathtaking views of the city skyline and the delicious local cuisine. This trip gave us a true feel for what Pittsburgh has to offer. Highly recommended for anyone looking to explore this underrated city!"
    )
    review16 = Review(
        user_id=4,
        itinerary_id=9,
        review="The Sequoia and Kings Canyon National Parks Trip was absolutely stunning! The giant sequoias are a sight to behold, and the peaceful meadows and scenic vistas made for an unforgettable experience. The itinerary was well-paced, giving us enough time to explore the highlights without feeling rushed. Perfect for nature lovers who want to immerse themselves in the beauty of these incredible parks!"
    )
    review17 = Review(
        user_id=5,
        itinerary_id=10,
        review="While the scenery at Sequoia and Kings Canyon National Parks was breathtaking, the trip was less enjoyable because of the huge crowds. We visited during a holiday weekend, and it was challenging to find parking, and the trails were packed with people. It took away from the serene experience we were hoping for. If you plan to visit, I suggest going during off-peak times to avoid the crowds."
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review9)
    db.session.add(review10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)
    db.session.add(review14)
    db.session.add(review15)
    db.session.add(review16)
    db.session.add(review17)
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
