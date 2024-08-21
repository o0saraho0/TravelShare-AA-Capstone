from app.models import db, environment, SCHEMA, Activity
from sqlalchemy.sql import text


def seed_activities():
    activity1 = Activity(
        place = "West Lake",
        longitude = 120.144128,
        latitude = 30.243945,
        description = "Start your exploration at West Lake, the most famous attraction in Hangzhou. Take a leisurely walk or rent a bike to explore the scenic area. Enjoy a boat ride on West Lake to see iconic spots like Three Pools Mirroring the Moon and Broken Bridge.",
        place_image_url = "/images/Hangzhou1_01.jpg",
        schedule_id = 1
    )
    activity2 = Activity(
        place = "Impression West Lake Show",
        longitude =  120.138635,
        latitude = 30.256339,
        description = "Watch this spectacular evening show on the lake, featuring lights, music, and dance.",
        place_image_url = "/images/Hangzhou1_02.webp",
        schedule_id = 1
    )
    activity3 = Activity(
        place = "Lingyin Temple",
        longitude= 120.0896,
        latitude= 30.2458,
        description = "Visit this ancient Buddhist temple, one of the largest and wealthiest in China. Explore the Feilai Feng grottoes nearby.",
        place_image_url = "/images/Hangzhou2_01.jpg",
        schedule_id = 2
    )
    activity4 = Activity(
        place = "Longjing Tea Plantations",
        longitude=120.0975,
        latitude=30.2298,
        description = "Head to the Longjing Tea Plantations, where you can tour the fields, learn about tea production, and taste fresh Longjing (Dragon Well) tea.",
        place_image_url = "/images/Hangzhou2_02.jpg",
        schedule_id = 2
    )
    activity5 = Activity(
        place = "Nine Creeks and Eighteen Gullies",
        longitude=120.1073,
        latitude=30.2235,
        description = "Hike through this beautiful scenic area, known for its lush greenery, babbling brooks, and serene environment.",
        place_image_url = "/images/Hangzhou3_01.webp",
        schedule_id = 3
    )
    activity6 = Activity(
        place = "Huagang (Flower Harbor) Park",
        longitude = 120.1298,
        latitude = 30.2296,
        description = "Visit this picturesque park at the southwest end of West Lake, known for its colorful flowers and koi fish ponds.",
        place_image_url = "/images/Hangzhou3_02.jpg",
        schedule_id = 3
    )
    activity7 = Activity(
        place = "Xixi National Wetland Park",
        longitude = 120.0848,
        latitude = 30.2656,
        description = "Visit the park for an evening boat ride through the wetlands, enjoying the natural beauty and tranquility.",
        place_image_url = "/images/Hangzhou3_03.jpg",
        schedule_id = 3
    )
    activity8 = Activity(
        place = "China National Silk Museum",
        longitude = 120.1622,
        latitude = 30.2268,
        description = "Explore the largest silk museum in the world, where you can learn about the history of silk in China and see beautiful silk garments.",
        place_image_url = "/images/Hangzhou4_01.jpg",
        schedule_id = 4
    )
    activity9 = Activity(
        place = "Hangzhou Botanical Garden",
        longitude = 120.1265,
        latitude = 30.2671,
        description = "Wander through the lush gardens and see a variety of plant species.",
        place_image_url = "/images/Hangzhou4_02.webp",
        schedule_id = 4
    )
    activity10 = Activity(
        place = "Night Market",
        longitude = 120.1822,
        latitude = 30.2675,
        description = "Explore one of Hangzhou's night markets for shopping and street food.",
        place_image_url = "/images/Hangzhou4_03.png",
        schedule_id = 4
    )
    activity11 = Activity(
        place = "Wuzhen Water Town",
        longitude = 120.4853,
        latitude = 30.7437,
        description = "Take a day trip to Wuzhen, one of the most famous water towns in China. Wander through the ancient streets, cross stone bridges, and enjoy the traditional architecture.",
        place_image_url = "/images/Hangzhou5_01.jpg",
        schedule_id = 5
    )
    activity12 = Activity(
        place = "West Lake",
        longitude = 120.1509,
        latitude = 30.2439,
        description = "Start your exploration at West Lake, the most famous attraction in Hangzhou. Take a leisurely walk or rent a bike to explore the scenic area. Enjoy a boat ride on West Lake to see iconic spots like Three Pools Mirroring the Moon and Broken Bridge.",
        place_image_url = "/images/Hangzhou1_01.jpg",
        schedule_id = 6
    )
    activity13 = Activity(
        place = "Impression West Lake Show",
        longitude = 120.1419,
        latitude = 30.2545,
        description = "Watch this spectacular evening show on the lake, featuring lights, music, and dance.",
        place_image_url = "/images/Hangzhou1_02.webp",
        schedule_id = 6
    )
    activity14 = Activity(
        place = "Lingyin Temple",
        longitude = 120.0896,
        latitude = 30.2458,
        description = "Visit this ancient Buddhist temple, one of the largest and wealthiest in China. Explore the Feilai Feng grottoes nearby.",
        place_image_url = "/images/Hangzhou2_01.jpg",
        schedule_id = 7
    )
    activity15 = Activity(
        place = "Longjing Tea Plantations",
        longitude = 120.0975,
        latitude = 30.2298,
        description = "Head to the Longjing Tea Plantations, where you can tour the fields, learn about tea production, and taste fresh Longjing (Dragon Well) tea.",
        place_image_url = "/images/Hangzhou2_02.jpg",
        schedule_id = 7
    )
    activity16 = Activity(
        place = "Hangzhou Botanical Garden",
        longitude = 120.1265,
        latitude = 30.2671,
        description = "Wander through the lush gardens and see a variety of plant species.",
        place_image_url = "/images/Hangzhou4_02.webp",
        schedule_id = 8
    )
    activity17 = Activity(
        place = "Xixi National Wetland Park",
        longitude = 120.0848,
        latitude = 30.2656,
        description = "Visit the park for an evening boat ride through the wetlands, enjoying the natural beauty and tranquility.",
        place_image_url = "/images/Hangzhou3_03.jpg",
        schedule_id = 8
    )
    activity18 = Activity(
        place = "The Bund",
        longitude = 121.4910,
        latitude = 31.2400,
        description = "Start your day with a stroll along The Bund, Shanghai's historic waterfront area. Enjoy views of the iconic skyline and colonial architecture.",
        place_image_url = "/images/Shanghai1_01.jpg",
        schedule_id = 9
    )
    activity19 = Activity(
        place = "Yu Garden",
        longitude = 121.4940,
        latitude = 31.2253,
        description = "Head to the old town and visit the beautifully preserved classical Chinese garden. Explore the nearby bazaar for souvenirs and snacks.",
        place_image_url = "/images/Shanghai1_02.jpg",
        schedule_id = 9
    )
    activity20 = Activity(
        place = "Nanjing Road",
        longitude = 121.4811,
        latitude = 31.2334,
        description = "Walk along this bustling shopping street and grab lunch at one of the many local eateries.",
        place_image_url = "/images/Shanghai1_03.jpg",
        schedule_id = 9
    )
    activity21 = Activity(
        place = "Jade Buddha Temple",
        longitude = 121.4489,
        latitude = 31.2424,
        description = "Visit this active Buddhist temple, home to two jade Buddha statues. It's a peaceful retreat in the middle of the city.",
        place_image_url = "/images/Shanghai2_01.jpg",
        schedule_id = 10
    )
    activity22 = Activity(
        place = "Shanghai Tower",
        longitude = 121.5016,
        latitude = 31.2336,
        description = "Head to Lujiazui in Pudong and visit the Shanghai Tower, the tallest building in China. Take the elevator to the observation deck for a breathtaking view of the city.",
        place_image_url = "/images/Shanghai2_02.webp",
        schedule_id = 10
    )
    activity23 = Activity(
        place = "Shanghai World Financial Center",
        longitude = 121.5014,
        latitude = 31.2347,
        description = "Nearby, you can also visit the SWFC for another sky-high view and unique architecture.",
        place_image_url = "/images/Shanghai3_03.jpg",
        schedule_id = 10
    )
    activity24 = Activity(
        place = "Jing'an Temple",
        longitude = 121.4450,
        latitude = 31.2235,
        description = "Stop by this serene Buddhist temple with its striking golden roofs. It's a beautiful contrast to the surrounding modern skyscrapers.",
        place_image_url = "/images/Shanghai3_01.jpg",
        schedule_id = 11
    )
    activity25 = Activity(
        place = "Tulum Archaeological Zone (Tulum Ruins)",
        longitude = -87.4623,
        latitude = 20.2132,
        description = "Explore the ancient Mayan city located on the cliffs overlooking the Caribbean Sea. The ruins offer stunning views and a glimpse into Mayan history and culture.",
        place_image_url = "/images/Mexico1_01.jpg",
        schedule_id = 12
    )
    activity26 = Activity(
        place = "SPER IK Lab",
        longitude = -87.4622,
        latitude = 20.2079,
        description = "Visit this contemporary art gallery set within a unique architectural space. The gallery features innovative exhibitions and installations that blend art with the natural environment.",
        place_image_url = "/images/Mexico1_02.jpg",
        schedule_id = 12
    )
    activity27 = Activity(
        place = "Chichén Itzá",
        longitude = -88.5678,
        latitude = 20.6829,
        description = "Discover one of the New Seven Wonders of the World, an iconic archaeological site featuring the Pyramid of Kukulcán, the Temple of the Warriors, and the Great Ball Court.",
        place_image_url = "/images/Mexico2_01.jpg",
        schedule_id = 13
    )
    activity28 = Activity(
        place = "Cenote Ik-Kil",
        longitude = -88.5504,
        latitude = 20.6741,
        description = "Swim in this beautiful open-air cenote located near Chichén Itzá. The cenote is surrounded by lush vegetation and offers crystal-clear waters perfect for a refreshing dip.",
        place_image_url = "/images/Mexico2_02.webp",
        schedule_id = 13
    )
    activity29 = Activity(
        place = "Cenote Saamal",
        longitude = -88.5932,
        latitude = 20.6900,
        description = "Visit this picturesque cenote known for its stunning turquoise waters and cascading waterfall. It's a great spot for swimming and photography.",
        place_image_url = "/images/Mexico2_03.webp",
        schedule_id = 13
    )
    activity30 = Activity(
        place = "Cenote Azul (Blue Cenote)",
        longitude = -87.2255,
        latitude = 20.5450,
        description = "Enjoy a relaxing day at this cenote, known for its clear blue waters and natural beauty. It's a popular spot for swimming, snorkeling, and diving.",
        place_image_url = "/images/Mexico3_01.jpg",
        schedule_id = 14
    )
    activity31 = Activity(
        place = "Cenote Manatí",
        longitude = -87.4454,
        latitude = 20.2439,
        description = "Also known as Casa Cenote, this cenote offers a unique experience with its mix of freshwater and seawater. It's a great place for snorkeling and observing marine life.",
        place_image_url = "/images/Mexico3_02.jpg",
        schedule_id = 14
    )
    activity32 = Activity(
        place = "XCaret",
        longitude = -87.4725,
        latitude = 20.5784,
        description = "Spend the day at this eco-archaeological park, which offers a mix of natural attractions, cultural performances, and adventure activities. Highlights include underground rivers, a coral reef aquarium, and a spectacular evening show.",
        place_image_url = "/images/Mexico4_01.webp",
        schedule_id = 15
    )
    activity33 = Activity(
        place = "Playa Delfines",
        longitude = -86.7523,
        latitude = 21.0467,
        description = "Relax on this beautiful public beach known for its soft white sand and stunning turquoise waters. It's a great spot for sunbathing, swimming, and enjoying the ocean views.",
        place_image_url = "/images/Mexico5_01.jpg",
        schedule_id = 16
    )
    activity34 = Activity(
        place = "Downtown",
        longitude = -86.8475,
        latitude = 21.1619,
        description = "Explore the vibrant downtown area of Cancun, where you can find local markets, restaurants, shops, and cultural attractions. It's a great place to experience the local culture and cuisine.",
        place_image_url = "/images/Mexico5_02.jpg",
        schedule_id = 16
    )
    activity35 = Activity(
        place = "Isla Mujeres",
        longitude = -86.7447,
        latitude = 21.2008,
        description = "Take a ferry to this charming island located off the coast of Cancun. Enjoy its beautiful beaches, snorkeling spots, and laid-back atmosphere. Visit Punta Sur, Garrafon Natural Reef Park, and explore the island by golf cart or bicycle.",
        place_image_url = "/images/Mexico6_01.webp",
        schedule_id = 17
    )
    activity36 = Activity(
        place = "Zion National Park",
        longitude = -113.0263,
        latitude = 37.2982,
        description = "The Canyon Overlook Trail is a short 1-mile round-trip hike that offers stunning views of Zion Canyon. The trail is moderate in difficulty and takes about 1 hour to complete. Lower Emerald Pool Trail is an easy 1.2-mile round-trip hike. The trail is family-friendly and offers beautiful views of the surrounding cliffs. You can extend the hike to the Upper Emerald Pools if you have more time.",
        place_image_url = "/images/Utah1.jpg",
        schedule_id = 18
    )
    activity37 = Activity(
        place = "Monument Valley",
        longitude = -110.1116,
        latitude = 36.9987,
        description = "Start your day with a scenic drive to Monument Valley. The drive takes about 3 hours from Zion National Park, so plan to leave early.",
        place_image_url = "/images/Utah1_02.jpg",
        schedule_id = 19
    )
    activity38 = Activity(
        place = "Forrest Gump Hill",
        longitude = -110.0833,
        latitude = 37.1018,
        description = "Upon arrival, visit the iconic Forrest Gump Hill, where the famous scene from the movie was filmed. Take some time to snap photos of the stunning landscape.",
        place_image_url = "/images/Utah2.jpg",
        schedule_id = 19
    )
    activity39 = Activity(
        place = "Dead Horse Point State Park",
        longitude = -109.7394,
        latitude = 38.4824,
        description = "The Dead Horse Point Overlook Trail: Hike the Dead Horse Point Overlook Trail, a 1.5-mile loop that offers breathtaking views of the Colorado River and the surrounding canyons.",
        place_image_url = "/images/Utah3_01.jpg",
        schedule_id = 20
    )
    activity40 = Activity(
        place = "Canyonlands National Park",
        longitude = -109.8214,
        latitude = 38.3269,
        description = "Start with a visit to Mesa Arch, a short 0.7-mile round-trip hike. The arch is particularly stunning at sunrise, but it’s beautiful at any time of day. Continue to the Grand View Point Overlook, where you can take a 2-mile round-trip hike along the rim of the canyon for panoramic views. End your day at the Green River Overlook, a viewpoint offering a spectacular view of the river winding through the canyon.",
        place_image_url = "/images/Utah3_02.jpg",
        schedule_id = 20
    )
    activity41 = Activity(
        place = "Arches National Park",
        longitude = -109.5925,
        latitude = 38.7331,
        description = "Start your day early with a visit to Balanced Rock, an iconic formation in the park. It’s a short walk from the parking area. Then head to The Windows Section, where you can explore the North and South Windows, as well as Double Arch. This area is great for photography, especially in the early morning light. After lunch, hike to Delicate Arch, the most famous arch in the park. The hike is 3 miles round-trip and moderately challenging, with a steady incline and some rocky sections. The arch is best photographed in the late afternoon or early evening.",
        place_image_url = "/images/Utah4.jpeg",
        schedule_id = 21
    )
    activity42 = Activity(
        place = "Capitol Reef National Park",
        longitude = -111.1681,
        latitude = 38.2833,
        description = "Start your day with a visit to Panorama Point for sweeping views of Capitol Reef’s colorful landscape. Then, head to The Castle, a prominent rock formation visible from the park’s main road. Visit the historic Fruita Schoolhouse to learn about the early settlers of the area. Then, stop by the Fremont Petroglyphs to see ancient rock art left by the Fremont people. End your day with a hike on the Hickman Bridge Trail, a 2-mile round-trip hike that takes you to a natural rock bridge. The hike is moderately challenging but offers great views along the way.",
        place_image_url = "/images/Utah5.jpg",
        schedule_id = 22
    )
    activity43 = Activity(
        place = "Bryce Canyon National Park",
        longitude = -112.1871,
        latitude = 37.5930,
        description = "Start your day with a visit to Bryce Point for one of the best views of the Bryce Amphitheater. The early morning light creates a stunning contrast between the red rock hoodoos and the deep blue sky. Hike the Queen’s Garden Trail, a 1.8-mile round-trip trail that descends into the Bryce Amphitheater. This trail is often combined with the Navajo Loop Trail for a more comprehensive experience. End your trip with a sunset at Sunset Point. The hoodoos glow in the soft light, creating a perfect ending to your Utah adventure.",
        place_image_url = "/images/Utah6.jpeg",
        schedule_id = 23
    )
    activity44 = Activity(
        place = "Carrizo Plain National Monument",
        longitude = -119.8099,
        latitude = 35.0917,
        description = "Start your day at Soda Lake, one of the largest alkaline lakes in California. The Soda Lake Overlook offers a great vantage point to see the expansive white salt flats. Take the short, easy trail to the overlook for panoramic views. Next, head to Painted Rock, a horseshoe-shaped sandstone formation with ancient pictographs created by the Chumash, Salinan, and Yokut tribes. You’ll need to check if guided tours are available, as access is sometimes restricted to protect the site. The hike to Painted Rock is about 2 miles round-trip. If you’re visiting in the spring, take some time to explore the wildflower fields that Carrizo Plain is famous for. The landscape transforms into a sea of vibrant colors, with blooms of goldfields, phacelia, and other native flowers. Popular spots for wildflower viewing include the eastern foothills of the Caliente Range and the Temblor Range.",
        place_image_url = "/images/California1.jpeg",
        schedule_id = 24
    )
    activity45 = Activity(
        place = "Antelope Valley California Poppy Reserve State Natural Reserve",
        longitude = -118.3893,
        latitude = 34.7268,
        description = "Start your day early and drive to Antelope Valley California Poppy Reserve. The reserve is particularly stunning in the spring when the poppies are in full bloom. Aim to arrive early to beat the crowds and catch the flowers opening in the morning sunlight. Explore the various trails within the reserve. The South and North Poppy Loop Trails are popular and provide easy to moderate hikes with excellent views of the rolling hills covered in vibrant orange poppies. The entire loop is about 3.3 miles, but shorter sections can be done if preferred.",
        place_image_url = "/images/California2.jpg",
        schedule_id = 25
    )
    activity46 = Activity(
        place = "San Francisco",
        longitude = -122.4194,
        latitude = 37.7749,
        description = "Start your trip in San Francisco. Consider spending some time exploring iconic spots like the Golden Gate Bridge, Fisherman’s Wharf, or Alcatraz Island if you haven’t already.",
        place_image_url = "/images/CaliforniaHW1_01.webp",
        schedule_id = 26
    )
    activity47 = Activity(
        place = "Pacifica",
        longitude = -122.4869,
        latitude = 37.6138,
        description = "Begin your drive south on Highway 1. Stop in Pacifica for a quick hike along the Devil’s Slide Trail, a 1.3-mile paved trail with stunning ocean views.",
        place_image_url = "/images/CaliforniaHW1_02.webp",
        schedule_id = 26
    )
    activity48 = Activity(
        place = "Half Moon Bay",
        longitude = -122.4286,
        latitude = 37.4636,
        description = "Continue to Half Moon Bay, known for its dramatic coastal cliffs and beaches. Visit the famous Mavericks Beach, where big wave surfing competitions are held. Enjoy lunch at a local seafood spot, then visit the nearby Fitzgerald Marine Reserve to explore tide pools.",
        place_image_url = "/images/CaliforniaHW1_03.jpg",
        schedule_id = 26
    )
    activity49 = Activity(
        place = "Santa Cruz",
        longitude = -122.0308,
        latitude = 36.9741,
        description = "Arrive in Santa Cruz and check into your accommodations. Spend the evening strolling along the Santa Cruz Beach Boardwalk, one of California’s last remaining seaside amusement parks. Enjoy dinner at a local restaurant and take in the lively atmosphere.",
        place_image_url = "/images/CaliforniaHW1_04.jpg",
        schedule_id = 26
    )
    activity50 = Activity(
        place = "Monterey",
        longitude = -121.8947,
        latitude = 36.6002,
        description = "Drive south to Monterey, home to the world-renowned Monterey Bay Aquarium. Spend the morning exploring the aquarium or take a scenic drive along 17-Mile Drive, which offers incredible views of the Pacific Ocean, Pebble Beach, and the famous Lone Cypress.",
        place_image_url = "/images/CaliforniaHW2_01.jpeg",
        schedule_id = 27
    )
    activity51 = Activity(
        place = "Carmel-by-the-Sea",
        longitude = -121.9233,
        latitude = 36.5552,
        description = "Continue to Carmel-by-the-Sea, a charming town known for its art galleries and fairy-tale cottages. Take a walk along Carmel Beach, visit the historic Carmel Mission, or explore the shops and galleries in town. Enjoy lunch at one of Carmel’s many cozy cafes.",
        place_image_url = "/images/CaliforniaHW2_01.jpg",
        schedule_id = 27
    )
    activity52 = Activity(
        place = "Big Sur",
        longitude = -121.8058,
        latitude = 36.2704,
        description = "Drive into Big Sur, one of the most beautiful stretches of coastline in the world. Stop at Bixby Creek Bridge for a photo op and continue to your accommodations. Big Sur offers various options, from rustic cabins to luxury resorts. Spend the evening enjoying the tranquility of the area.",
        place_image_url = "/images/CaliforniaHW2_02.jpg",
        schedule_id = 27
    )
    activity53 = Activity(
        place = "Julia Pfeiffer Burns State Park",
        longitude = -121.6705,
        latitude = 36.1584,
        description = "Start your day with a visit to Julia Pfeiffer Burns State Park. Hike the McWay Falls Trail, a short and easy hike that leads to a viewpoint overlooking an 80-foot waterfall cascading onto the beach. This is one of Big Sur’s most iconic sights.",
        place_image_url = "/images/CaliforniaHW3_01.jpg",
        schedule_id = 28
    )
    activity54 = Activity(
        place = "Pfeiffer Beach",
        longitude = -121.7990,
        latitude = 36.2383,
        description = "Head to Pfeiffer Beach, known for its purple sand and unique rock formations. The beach is somewhat hidden, so keep an eye out for the narrow road leading to the parking area. Spend some time exploring the beach and taking in the stunning scenery.",
        place_image_url = "/images/CaliforniaHW3_02.jpg",
        schedule_id = 28
    )
    activity55 = Activity(
        place = "Ventana Wilderness",
        longitude = -121.6597,
        latitude = 36.2405,
        description = "If you’re up for more adventure, consider a hike in the Ventana Wilderness. The Ewoldsen Trail is a moderately challenging hike that offers fantastic views of the Big Sur coastline and redwood forests.",
        place_image_url = "/images/CaliforniaHW3_03.jpg",
        schedule_id = 28
    )
    activity56 = Activity(
        place = "Hearst Castle",
        longitude = -121.1664,
        latitude = 35.6852,
        description = "Drive south to San Simeon and visit Hearst Castle, the opulent estate of newspaper magnate William Randolph Hearst. Take a guided tour of the mansion and its beautiful gardens. The views of the coast from the castle are spectacular.",
        place_image_url = "/images/CaliforniaHW4_01.jpg",
        schedule_id = 29
    )
    activity57 = Activity(
        place = "Elephant Seal Rookery",
        longitude = -121.2837,
        latitude = 35.6652,
        description = "Just a short drive south of Hearst Castle, stop at the Elephant Seal Rookery at Piedras Blancas. Depending on the time of year, you can see hundreds of elephant seals lounging on the beach, an unforgettable wildlife experience.",
        place_image_url = "/images/CaliforniaHW4_02.jpg",
        schedule_id = 29
    )
    activity58 = Activity(
        place = "Cambria",
        longitude = -121.0814,
        latitude = 35.5641,
        description = "Continue to the charming town of Cambria. Take a stroll through the town’s quaint shops and art galleries or visit Moonstone Beach for a walk along the boardwalk. Enjoy lunch at a local café before continuing your journey.",
        place_image_url = "/images/CaliforniaHW4_03.png",
        schedule_id = 29
    )
    activity59 = Activity(
        place = "San Luis Obispo",
        longitude = -120.6602,
        latitude = 35.2828,
        description = "Arrive in San Luis Obispo, often called the “Happiest City in America.” Explore the downtown area, visit Mission San Luis Obispo de Tolosa, and enjoy a farm-to-table dinner at one of the city’s excellent restaurants.",
        place_image_url = "/images/CaliforniaHW4_04.jpg",
        schedule_id = 29
    )
    activity60 = Activity(
        place = "Pismo Beach",
        longitude = -120.6464,
        latitude = 35.1428,
        description = "Start your day with a visit to Pismo Beach, known for its wide sandy beaches and iconic pier. If you’re visiting in the right season, you can also stop by the Monarch Butterfly Grove to see thousands of butterflies clustered in the trees.",
        place_image_url = "/images/CaliforniaHW5_01.jpeg",
        schedule_id = 30
    )
    activity61 = Activity(
        place = "Solvang",
        longitude = -120.1376,
        latitude = 34.5958,
        description = "Continue south to Solvang, a charming Danish-style town in the Santa Ynez Valley. Explore the town’s unique architecture, visit a few of the many bakeries for authentic Danish pastries, and consider a quick visit to a local winery for a tasting.",
        place_image_url = "/images/CaliforniaHW5_04.jpg",
        schedule_id = 30
    )
    activity62 = Activity(
        place = "Santa Barbara",
        longitude = -119.6982,
        latitude = 34.4208,
        description = "Arrive in Santa Barbara, a city known for its Mediterranean-style architecture and beautiful beaches. Visit the historic Santa Barbara Mission, stroll along State Street for shopping and dining, and relax at the waterfront or on one of the city’s many beaches.",
        place_image_url = "/images/CaliforniaHW5_02.jpg",
        schedule_id = 30
    )
    activity63 = Activity(
        place = "Stearns Wharf",
        longitude = -119.6885,
        latitude = 34.4105,
        description = "End your trip with a sunset at Stearns Wharf, where you can enjoy views of the coastline and the Santa Ynez Mountains. Enjoy dinner at one of the waterfront restaurants and reflect on the incredible journey along Highway 1.",
        place_image_url = "/images/CaliforniaHW5_03.jpg",
        schedule_id = 30
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
    db.session.add(activity21)
    db.session.add(activity22)
    db.session.add(activity23)
    db.session.add(activity24)
    db.session.add(activity25)
    db.session.add(activity26)
    db.session.add(activity27)
    db.session.add(activity28)
    db.session.add(activity29)
    db.session.add(activity30)
    db.session.add(activity31)
    db.session.add(activity32)
    db.session.add(activity33)
    db.session.add(activity34)
    db.session.add(activity35)
    db.session.add(activity36)
    db.session.add(activity37)
    db.session.add(activity38)
    db.session.add(activity39)
    db.session.add(activity40)
    db.session.add(activity41)
    db.session.add(activity42)
    db.session.add(activity43)
    db.session.add(activity44)
    db.session.add(activity45)
    db.session.add(activity46)
    db.session.add(activity47)
    db.session.add(activity48)
    db.session.add(activity49)
    db.session.add(activity50)
    db.session.add(activity51)
    db.session.add(activity52)
    db.session.add(activity53)
    db.session.add(activity54)
    db.session.add(activity55)
    db.session.add(activity56)
    db.session.add(activity57)
    db.session.add(activity58)
    db.session.add(activity59)
    db.session.add(activity60)
    db.session.add(activity61)
    db.session.add(activity62)
    db.session.add(activity63)


    db.session.commit()


def undo_activities():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.activities RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM activities"))
        
    db.session.commit()
