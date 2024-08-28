from app.models import db, environment, SCHEMA, Itinerary
from sqlalchemy.sql import text


def seed_itineraries():
    itinerary1 = Itinerary(
        title="5 Days in Hangzhou",
        duration=5,
        description="Discover the serene beauty of Hangzhou over five enchanting days. This itinerary takes you through the city's most iconic sites, including the West Lake, Lingyin Temple, and the tea plantations of Longjing. Immerse yourself in the rich cultural heritage and tranquil landscapes that have inspired poets and artists for centuries.",
        preview_image_url="/images/Hangzhou1_01.jpg",
        traveler_id=1,
        category_id=1,
    )
    itinerary2 = Itinerary(
        title="3 Days in Hangzhou",
        duration=3,
        description="A short yet fulfilling getaway to Hangzhou, this three-day itinerary is perfect for those looking to experience the city's highlights. Visit the picturesque West Lake, explore the bustling Hefang Street, and unwind at the famous tea houses. This is an ideal trip for first-time visitors or those on a tight schedule.",
        preview_image_url="/images/Hangzhou2_01.jpg",
        traveler_id=2,
        category_id=1,
    )
    itinerary3 = Itinerary(
        title="Wandering in Shanghai",
        duration=3,
        description="Experience the vibrant energy of Shanghai with this three-day itinerary. Explore the blend of modernity and tradition as you visit landmarks like the Bund, Yu Garden, and the futuristic skyline of Pudong. From historical sites to cutting-edge architecture, this itinerary showcases the best of Shanghai.",
        preview_image_url="/images/Shanghai2_02.webp",
        traveler_id=3,
        category_id=1,
    )
    itinerary4 = Itinerary(
        title="6 Days in Tulum and Cancun",
        duration=6,
        description="Enjoy the perfect mix of relaxation and adventure with this six-day itinerary in Tulum and Cancun. Explore ancient Mayan ruins, snorkel in crystal-clear cenotes, and unwind on the white sandy beaches. Whether you're seeking culture, nature, or just a tropical escape, this itinerary offers it all.",
        preview_image_url="/images/Mexico4_01.webp",
        traveler_id=4,
        category_id=2,
    )
    itinerary5 = Itinerary(
        title="Ultimate Utah National Parks Road Trip",
        duration=6,
        description="Embark on an unforgettable road trip through Utah's most stunning national parks. This itinerary guides you through Zion, Bryce Canyon, Arches, Canyonlands, and Capitol Reef, offering breathtaking landscapes, scenic hikes, and unforgettable experiences in the heart of America's desert wilderness.",
        preview_image_url="/images/Utah4.jpeg",
        traveler_id=5,
        category_id=3,
    )
    itinerary6 = Itinerary(
        title="California Wildflower Road Trip",
        duration=2,
        description="Witness the vibrant explosion of wildflowers across California's landscapes with this road trip itinerary. From the Carrizo Plain to the Antelope Valley, this journey captures the fleeting beauty of spring blooms, offering stunning photo opportunities and serene drives through some of the state's most picturesque areas.",
        preview_image_url="/images/California2.jpg",
        traveler_id=2,
        category_id=3,
    )
    itinerary7 = Itinerary(
        title="Pacific Coast Highway Road Trip",
        duration=6,
        description="Cruise along the iconic Pacific Coast Highway with this road trip itinerary, which takes you from the scenic cliffs of Big Sur to the charming coastal towns of California. Experience the rugged coastline, breathtaking ocean views, and must-see stops like Monterey, Santa Barbara, and Malibu.",
        preview_image_url="/images/CaliforniaHW1_01.webp",
        traveler_id=1,
        category_id=3,
    )
    itinerary8 = Itinerary(
        title="Hawaii Family Vacation",
        duration=5,
        description="Enjoy a memorable family vacation in Hawaii with a blend of adventure, relaxation, and cultural experiences. From hiking the iconic Diamond Head to exploring the beautiful beaches and historic sites like Pearl Harbor, this itinerary offers something for everyone.",
        preview_image_url="/images/Hawaii.jpg",
        traveler_id=6,
        category_id=2,
    )
    itinerary9 = Itinerary(
        title="Pittsburgh Cultural and Scenic Trip",
        duration=4,
        description="Explore the cultural, historical, and scenic highlights of Pittsburgh. From iconic landmarks like the Duquesne Incline and the Cathedral of Learning to delicious local cuisine and memorable activities, this itinerary offers a comprehensive Pittsburgh experience.",
        preview_image_url="/images/Pittsburgh4_01.jpg",
        traveler_id=7,
        category_id=1,
    )
    itinerary10 = Itinerary(
        title="Sequoia and Kings Canyon National Parks Trip",
        duration=2,
        description="Discover the majestic beauty of Sequoia and Kings Canyon National Parks over two days. Explore the towering giant sequoias, breathtaking vistas, and serene meadows that make these parks a must-visit destination for nature lovers.",
        preview_image_url="/images/Tree1_02.jpg",
        traveler_id=8,
        category_id=2,
    )

    db.session.add(itinerary1)
    db.session.add(itinerary2)
    db.session.add(itinerary3)
    db.session.add(itinerary4)
    db.session.add(itinerary5)
    db.session.add(itinerary6)
    db.session.add(itinerary7)
    db.session.add(itinerary8)
    db.session.add(itinerary9)
    db.session.add(itinerary10)
    db.session.commit()


def undo_itineraries():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.itineraries RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM itineraries"))

    db.session.commit()
