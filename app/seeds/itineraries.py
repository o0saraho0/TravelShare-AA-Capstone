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
        traveler_id=6,
        category_id=3,
    )
    itinerary8 = Itinerary(
        title="Hawaii Family Vacation",
        duration=5,
        description="Enjoy a memorable family vacation in Hawaii with a blend of adventure, relaxation, and cultural experiences. From hiking the iconic Diamond Head to exploring the beautiful beaches and historic sites like Pearl Harbor, this itinerary offers something for everyone.",
        preview_image_url="/images/Hawaii.jpg",
        traveler_id=1,
        category_id=2,
    )
    itinerary9 = Itinerary(
        title="Pittsburgh Cultural and Scenic Trip",
        duration=4,
        description="Explore the cultural, historical, and scenic highlights of Pittsburgh. From iconic landmarks like the Duquesne Incline and the Cathedral of Learning to delicious local cuisine and memorable activities, this itinerary offers a comprehensive Pittsburgh experience.",
        preview_image_url="/images/Pittsburgh4_01.jpg",
        traveler_id=1,
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
    itinerary11 = Itinerary(
        title="Get Lost in Los Angeles",
        duration=2,
        description="The city of stars and angels, Los Angeles is a vibrant metropolis where dreams come true and creativity thrives. With its iconic landmarks, diverse neighborhoods, and world-renowned entertainment, LA offers a plethora of activities that ensure you’ll never run out of things to do. Whether you’re strolling along the Hollywood Walk of Fame, catching a breathtaking sunset at Santa Monica Pier, exploring the eclectic boutiques of Venice Beach, or indulging in world-class cuisine in Downtown LA, there’s something for everyone. Get ready for an unforgettable adventure in the heart of Los Angeles!",
        preview_image_url="/images/LA1_02.jpg",
        traveler_id=2,
        category_id=1,
    )
    itinerary12 = Itinerary(
        title="New York! New York!",
        duration=2,
        description="Experience the electrifying energy of New York City over two unforgettable days. Begin with a stroll through Central Park, where you can relax by the lake, visit the zoo, or enjoy a picnic on the great lawn. Explore the iconic landmarks of Times Square, the Empire State Building, and Rockefeller Center. Discover the rich history at the Statue of Liberty and Ellis Island, then immerse yourself in the cultural offerings of the Metropolitan Museum of Art and the American Museum of Natural History. End your days with a Broadway show and dining at some of NYC's finest restaurants.",
        preview_image_url="/images/NY1_02.jpg",
        traveler_id=5,
        category_id=1,
    )
    itinerary13 = Itinerary(
        title="A Weekend in Boston",
        duration=2,
        description="Step back in time as you explore the historic charm of Boston, a city rich with American history and cultural heritage. Walk along the Freedom Trail, visiting key landmarks such as Paul Revere's House, the Old North Church, and the Boston Tea Party Ships and Museum. Take in the beauty of the Boston Public Garden, enjoy a boat ride on the famous Swan Boats, and explore the bustling neighborhoods of Beacon Hill and the North End. Don't miss the chance to visit prestigious universities like Harvard and MIT, and end your day with a relaxing evening on the waterfront.",
        preview_image_url="/images/Boston1_02.jpg",
        traveler_id=5,
        category_id=1,
    )
    itinerary14 = Itinerary(
        title="Yosemite Bliss: Nature's Playground",
        duration=2,
        description="Discover the awe-inspiring beauty of Yosemite National Park over a two-day exploration. Witness the grandeur of Yosemite Valley, home to famous landmarks such as El Capitan, Half Dome, and Bridalveil Fall. Hike through picturesque trails leading to majestic waterfalls, including the towering Yosemite Falls. Visit the tranquil Mariposa Grove, where you'll find ancient giant sequoias standing tall for centuries. Take in panoramic views from Glacier Point, and enjoy stargazing under the pristine night sky. Whether you're hiking, photographing, or simply relaxing, Yosemite offers a nature experience like no other.",
        preview_image_url="/images/Yosemite1_03.jpg",
        traveler_id=1,
        category_id=2,
    )
    itinerary15 = Itinerary(
        title="Jazz & Jambalaya: New Orleans Experience",
        duration=2,
        description="Immerse yourself in the vibrant culture of New Orleans, where music, food, and history come together in perfect harmony. Experience the soulful sounds of jazz at iconic venues on Frenchmen Street, and take a riverboat cruise along the Mississippi River. Visit the historic Garden District with its grand mansions and take a guided tour of the hauntingly beautiful cemeteries.",
        preview_image_url="/images/NO1_01.jpg",
        traveler_id=8,
        category_id=1,
    )
    itinerary16 = Itinerary(
        title="Tropical Getaway: 48 Hours in Key West",
        duration=2,
        description="Escape to the sun-soaked paradise of Key West, a tropical island renowned for its laid-back atmosphere, vibrant nightlife, and stunning natural beauty. Spend your days exploring the colorful coral reefs while snorkeling or diving, or take a relaxing boat tour to spot dolphins and sea turtles. Stroll down the famous Duval Street, lined with charming shops, lively bars, and historic landmarks like the Ernest Hemingway Home and Museum.",
        preview_image_url="/images/KeyWest1_03.jpg",
        traveler_id=7,
        category_id=2,
    )
    itinerary17 = Itinerary(
        title="Joshua Tree & Death Valley",
        duration=3,
        description="Venture into the captivating desert landscapes of Joshua Tree and Death Valley, where unique natural wonders await. In Joshua Tree, marvel at the twisted, otherworldly Joshua trees, massive boulders, and stunning rock formations. Take a hike through Hidden Valley and enjoy panoramic views from Keys View. Continue your journey to Death Valley, the hottest place on Earth, where you'll find dramatic sand dunes, salt flats, and the mesmerizing Artist's Palette. Visit Badwater Basin, the lowest point in North America, and experience the surreal beauty of this arid wonderland.",
        preview_image_url="/images/JoshuaTree1_03.webp",
        traveler_id=2,
        category_id=3,
    )
    itinerary18 = Itinerary(
        title="Lake Tahoe Retreat: Mountains & Clear Waters",
        duration=2,
        description="Escape to the serene beauty of Lake Tahoe, where crystal-clear waters and majestic mountains create the perfect backdrop for relaxation and adventure. Spend your days kayaking, paddleboarding, or simply lounging on the sandy beaches. In the winter, enjoy skiing and snowboarding at world-class resorts. Indulge in lakeside dining with fresh, locally-sourced cuisine and unwind with a sunset cruise on the tranquil waters of Lake Tahoe.",
        preview_image_url="/images/Tahoe1_01.webp",
        traveler_id=7,
        category_id=2,
    )
    itinerary19 = Itinerary(
        title="Urban Adventures - Toronto",
        duration=2,
        description="Explore the diverse and lively city of Toronto over a two-day adventure, where the city's vibrant atmosphere and cultural richness await you at every corner. Stroll through bustling urban streets lined with towering skyscrapers, iconic landmarks, and historic buildings that tell the story of the city's past.",
        preview_image_url="/images/Toronto1_01.webp",
        traveler_id=4,
        category_id=1,
    )
    itinerary20 = Itinerary(
        title="Shenzhen - City of Innovation",
        duration=2,
        description="Immerse yourself in the vibrant atmosphere of Shenzhen, a city known for its rapid development and innovative spirit. Over the course of two days, explore bustling districts filled with modern architecture, cutting-edge technology, and cultural attractions. Enjoy the fusion of traditional Chinese culture with the latest trends in fashion, art, and entertainment. Relax in beautiful parks and gardens, offering a peaceful escape from the city's energetic pace.",
        preview_image_url="/images/Shenzhen1_01.jpg",
        traveler_id=3,
        category_id=1,
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
    db.session.add(itinerary11)
    db.session.add(itinerary12)
    db.session.add(itinerary13)
    db.session.add(itinerary14)
    db.session.add(itinerary15)
    db.session.add(itinerary16)
    db.session.add(itinerary17)
    db.session.add(itinerary18)
    db.session.add(itinerary19)
    db.session.add(itinerary20)
    db.session.commit()


def undo_itineraries():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.itineraries RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM itineraries"))

    db.session.commit()
