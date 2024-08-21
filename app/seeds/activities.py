from app.models import db, environment, SCHEMA, Activity
from sqlalchemy.sql import text


def seed_activities():
    activity1 = Activity(
        place = "West Lake",
        description = "Start your exploration at West Lake, the most famous attraction in Hangzhou. Take a leisurely walk or rent a bike to explore the scenic area. Enjoy a boat ride on West Lake to see iconic spots like Three Pools Mirroring the Moon and Broken Bridge.",
        place_image_url = "/images/Hangzhou1_01.jpg",
        schedule_id = 1
    )
    activity2 = Activity(
        place = "Impression West Lake Show",
        description = "Watch this spectacular evening show on the lake, featuring lights, music, and dance.",
        place_image_url = "/images/Hangzhou1_02.webp",
        schedule_id = 1

    )
    activity3 = Activity(
        place = "Lingyin Temple",
        description = "Visit this ancient Buddhist temple, one of the largest and wealthiest in China. Explore the Feilai Feng grottoes nearby.",
        place_image_url = "/images/Hangzhou2_01.jpg",
        schedule_id = 2
    )
    activity4 = Activity(
        place = "Longjing Tea Plantations",
        description = "Head to the Longjing Tea Plantations, where you can tour the fields, learn about tea production, and taste fresh Longjing (Dragon Well) tea.",
        place_image_url = "/images/Hangzhou2_02.jpg",
        schedule_id = 2
    )
    activity5 = Activity(
        place = "Nine Creeks and Eighteen Gullies",
        description = "Hike through this beautiful scenic area, known for its lush greenery, babbling brooks, and serene environment.",
        place_image_url = "/images/Hangzhou3_01.webp",
        schedule_id = 3
    )
    activity6 = Activity(
        place = "Huagang (Flower Harbor) Park",
        description = "Visit this picturesque park at the southwest end of West Lake, known for its colorful flowers and koi fish ponds.",
        place_image_url = "/images/Hangzhou3_02.jpg",
        schedule_id = 3
    )
    activity7 = Activity(
        place = "Xixi National Wetland Park",
        description = "Visit the park for an evening boat ride through the wetlands, enjoying the natural beauty and tranquility.",
        place_image_url = "/images/Hangzhou3_03.jpg",
        schedule_id = 3
    )
    activity8 = Activity(
        place = "China National Silk Museum",
        description = "Explore the largest silk museum in the world, where you can learn about the history of silk in China and see beautiful silk garments.",
        place_image_url = "/images/Hangzhou4_01.jpg",
        schedule_id = 4
    )
    activity9 = Activity(
        place = "Hangzhou Botanical Garden",
        description = "Wander through the lush gardens and see a variety of plant species.",
        place_image_url = "/images/Hangzhou4_02.webp",
        schedule_id = 4
    )
    activity10 = Activity(
        place = "Night Market",
        description = "Explore one of Hangzhou's night markets for shopping and street food.",
        place_image_url = "/images/Hangzhou4_03.png",
        schedule_id = 4
    )
    activity11 = Activity(
        place = "Wuzhen Water Town",
        description = "Take a day trip to Wuzhen, one of the most famous water towns in China. Wander through the ancient streets, cross stone bridges, and enjoy the traditional architecture.",
        place_image_url = "/images/Hangzhou5_01.jpg",
        schedule_id = 5
    )
    activity12 = Activity(
        place = "West Lake",
        description = "Start your exploration at West Lake, the most famous attraction in Hangzhou. Take a leisurely walk or rent a bike to explore the scenic area. Enjoy a boat ride on West Lake to see iconic spots like Three Pools Mirroring the Moon and Broken Bridge.",
        place_image_url = "/images/Hangzhou1_01.jpg",
        schedule_id = 6
    )
    activity13 = Activity(
        place = "Impression West Lake Show",
        description = "Watch this spectacular evening show on the lake, featuring lights, music, and dance.",
        place_image_url = "/images/Hangzhou1_02.webp",
        schedule_id = 6
    )
    activity14 = Activity(
        place = "Lingyin Temple",
        description = "Visit this ancient Buddhist temple, one of the largest and wealthiest in China. Explore the Feilai Feng grottoes nearby.",
        place_image_url = "images/Hangzhou2_01.jpg",
        schedule_id = 7
    )
    activity15 = Activity(
        place = "Longjing Tea Plantations",
        description = "Head to the Longjing Tea Plantations, where you can tour the fields, learn about tea production, and taste fresh Longjing (Dragon Well) tea.",
        place_image_url = "/images/Hangzhou2_02.jpg",
        schedule_id = 7
    )
    activity16 = Activity(
        place = "Hangzhou Botanical Garden",
        description = "Wander through the lush gardens and see a variety of plant species.",
        place_image_url = "/images/Hangzhou4_02.webp",
        schedule_id = 8
    )
    activity17 = Activity(
        place = "Xixi National Wetland Park",
        description = "Visit the park for an evening boat ride through the wetlands, enjoying the natural beauty and tranquility.",
        place_image_url = "/images/Hangzhou3_03.jpg",
        schedule_id = 8
    )
    activity18 = Activity(
        place = "The Bund",
        description = "Start your day with a stroll along The Bund, Shanghai's historic waterfront area. Enjoy views of the iconic skyline and colonial architecture.",
        place_image_url = "/images/Shanghai1_01.jpg",
        schedule_id = 9
    )
    activity19 = Activity(
        place = "Yu Garden",
        description = "Head to the old town and visit the beautifully preserved classical Chinese garden. Explore the nearby bazaar for souvenirs and snacks.",
        place_image_url = "/images/Shanghai1_02.jpg",
        schedule_id = 9
    )
    activity20 = Activity(
        place = "Nanjing Road",
        description = "Walk along this bustling shopping street and grab lunch at one of the many local eateries.",
        place_image_url = "/images/Shanghai1_03.jpg",
        schedule_id = 9
    )

    db.session.add(activity1)
    db.session.add(activity2)
    db.session.add(activity3)
    db.session.add(activity4)
    db.session.add(activity5)
    db.session.add(activity6)
    db.session.add(activity7)
    db.session.add(activity8)
    db.session.add(activity9)
    db.session.add(activity10)
    db.session.add(activity11)
    db.session.add(activity12)
    db.session.add(activity13)
    db.session.add(activity14)
    db.session.add(activity15)
    db.session.add(activity16)
    db.session.add(activity17)
    db.session.add(activity18)
    db.session.add(activity19)
    db.session.add(activity20)


    db.session.commit()


def undo_activities():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.activities RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM activities"))
        
    db.session.commit()
