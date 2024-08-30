from app.models import db, environment, SCHEMA, Activity
from sqlalchemy.sql import text


def seed_activities():
    activity1 = Activity(
        place="West Lake",
        longitude=120.144128,
        latitude=30.243945,
        description="Start your exploration at West Lake, the most famous attraction in Hangzhou. Take a leisurely walk or rent a bike to explore the scenic area. Enjoy a boat ride on West Lake to see iconic spots like Three Pools Mirroring the Moon and Broken Bridge.",
        place_image_url="/images/Hangzhou1_01.jpg",
        schedule_id=1
    )
    activity2 = Activity(
        place="Impression West Lake Show",
        longitude=120.138635,
        latitude=30.256339,
        description="Watch this spectacular evening show on the lake, featuring lights, music, and dance.",
        place_image_url="/images/Hangzhou1_02.webp",
        schedule_id=1
    )
    activity3 = Activity(
        place="Lingyin Temple",
        longitude=120.0896,
        latitude=30.2458,
        description="Visit this ancient Buddhist temple, one of the largest and wealthiest in China. Explore the Feilai Feng grottoes nearby.",
        place_image_url="/images/Hangzhou2_01.jpg",
        schedule_id=2
    )
    activity4 = Activity(
        place="Longjing Tea Plantations",
        longitude=120.0975,
        latitude=30.2298,
        description="Head to the Longjing Tea Plantations, where you can tour the fields, learn about tea production, and taste fresh Longjing (Dragon Well) tea.",
        place_image_url="/images/Hangzhou2_02.jpg",
        schedule_id=2
    )
    activity5 = Activity(
        place="Nine Creeks and Eighteen Gullies",
        longitude=120.1073,
        latitude=30.2235,
        description="Hike through this beautiful scenic area, known for its lush greenery, babbling brooks, and serene environment.",
        place_image_url="/images/Hangzhou3_01.webp",
        schedule_id=3
    )
    activity6 = Activity(
        place="Huagang (Flower Harbor) Park",
        longitude=120.1298,
        latitude=30.2296,
        description="Visit this picturesque park at the southwest end of West Lake, known for its colorful flowers and koi fish ponds.",
        place_image_url="/images/Hangzhou3_02.jpg",
        schedule_id=3
    )
    activity7 = Activity(
        place="Xixi National Wetland Park",
        longitude=120.0848,
        latitude=30.2656,
        description="Visit the park for an evening boat ride through the wetlands, enjoying the natural beauty and tranquility.",
        place_image_url="/images/Hangzhou3_03.jpg",
        schedule_id=3
    )
    activity8 = Activity(
        place="China National Silk Museum",
        longitude=120.1622,
        latitude=30.2268,
        description="Explore the largest silk museum in the world, where you can learn about the history of silk in China and see beautiful silk garments.",
        place_image_url="/images/Hangzhou4_01.jpg",
        schedule_id=4
    )
    activity9 = Activity(
        place="Hangzhou Botanical Garden",
        longitude=120.1265,
        latitude=30.2671,
        description="Wander through the lush gardens and see a variety of plant species.",
        place_image_url="/images/Hangzhou4_02.webp",
        schedule_id=4
    )
    activity10 = Activity(
        place="Night Market",
        longitude=120.1822,
        latitude=30.2675,
        description="Explore one of Hangzhou's night markets for shopping and street food.",
        place_image_url="/images/Hangzhou4_03.png",
        schedule_id=4
    )
    activity11 = Activity(
        place="Wuzhen Water Town",
        longitude=120.4853,
        latitude=30.7437,
        description="Take a day trip to Wuzhen, one of the most famous water towns in China. Wander through the ancient streets, cross stone bridges, and enjoy the traditional architecture.",
        place_image_url="/images/Hangzhou5_01.jpg",
        schedule_id=5
    )
    activity12 = Activity(
        place="West Lake",
        longitude=120.1509,
        latitude=30.2439,
        description="Start your exploration at West Lake, the most famous attraction in Hangzhou. Take a leisurely walk or rent a bike to explore the scenic area. Enjoy a boat ride on West Lake to see iconic spots like Three Pools Mirroring the Moon and Broken Bridge.",
        place_image_url="/images/Hangzhou1_01.jpg",
        schedule_id=6
    )
    activity13 = Activity(
        place="Impression West Lake Show",
        longitude=120.1419,
        latitude=30.2545,
        description="Watch this spectacular evening show on the lake, featuring lights, music, and dance.",
        place_image_url="/images/Hangzhou1_02.webp",
        schedule_id=6
    )
    activity14 = Activity(
        place="Lingyin Temple",
        longitude=120.0896,
        latitude=30.2458,
        description="Visit this ancient Buddhist temple, one of the largest and wealthiest in China. Explore the Feilai Feng grottoes nearby.",
        place_image_url="/images/Hangzhou2_01.jpg",
        schedule_id=7
    )
    activity15 = Activity(
        place="Longjing Tea Plantations",
        longitude=120.0975,
        latitude=30.2298,
        description="Head to the Longjing Tea Plantations, where you can tour the fields, learn about tea production, and taste fresh Longjing (Dragon Well) tea.",
        place_image_url="/images/Hangzhou2_02.jpg",
        schedule_id=7
    )
    activity16 = Activity(
        place="Hangzhou Botanical Garden",
        longitude=120.1265,
        latitude=30.2671,
        description="Wander through the lush gardens and see a variety of plant species.",
        place_image_url="/images/Hangzhou4_02.webp",
        schedule_id=8
    )
    activity17 = Activity(
        place="Xixi National Wetland Park",
        longitude=120.0848,
        latitude=30.2656,
        description="Visit the park for an evening boat ride through the wetlands, enjoying the natural beauty and tranquility.",
        place_image_url="/images/Hangzhou3_03.jpg",
        schedule_id=8
    )
    activity18 = Activity(
        place="The Bund",
        longitude=121.4910,
        latitude=31.2400,
        description="Start your day with a stroll along The Bund, Shanghai's historic waterfront area. Enjoy views of the iconic skyline and colonial architecture.",
        place_image_url="/images/Shanghai1_01.jpg",
        schedule_id=9
    )
    activity19 = Activity(
        place="Yu Garden",
        longitude=121.4940,
        latitude=31.2253,
        description="Head to the old town and visit the beautifully preserved classical Chinese garden. Explore the nearby bazaar for souvenirs and snacks.",
        place_image_url="/images/Shanghai1_02.jpg",
        schedule_id=9
    )
    activity20 = Activity(
        place="Nanjing Road",
        longitude=121.4811,
        latitude=31.2334,
        description="Walk along this bustling shopping street and grab lunch at one of the many local eateries.",
        place_image_url="/images/Shanghai1_03.jpg",
        schedule_id=9
    )
    activity21 = Activity(
        place="Jade Buddha Temple",
        longitude=121.4489,
        latitude=31.2424,
        description="Visit this active Buddhist temple, home to two jade Buddha statues. It's a peaceful retreat in the middle of the city.",
        place_image_url="/images/Shanghai2_01.jpg",
        schedule_id=10
    )
    activity22 = Activity(
        place="Shanghai Tower",
        longitude=121.5016,
        latitude=31.2336,
        description="Head to Lujiazui in Pudong and visit the Shanghai Tower, the tallest building in China. Take the elevator to the observation deck for a breathtaking view of the city.",
        place_image_url="/images/Shanghai2_02.webp",
        schedule_id=10
    )
    activity23 = Activity(
        place="Shanghai World Financial Center",
        longitude=121.5014,
        latitude=31.2347,
        description="Nearby, you can also visit the SWFC for another sky-high view and unique architecture.",
        place_image_url="/images/Shanghai3_03.jpg",
        schedule_id=10
    )
    activity24 = Activity(
        place="Jing'an Temple",
        longitude=121.4450,
        latitude=31.2235,
        description="Stop by this serene Buddhist temple with its striking golden roofs. It's a beautiful contrast to the surrounding modern skyscrapers.",
        place_image_url="/images/Shanghai3_01.jpg",
        schedule_id=11
    )
    activity25 = Activity(
        place="Tulum Archaeological Zone (Tulum Ruins)",
        longitude=-87.4623,
        latitude=20.2132,
        description="Explore the ancient Mayan city located on the cliffs overlooking the Caribbean Sea. The ruins offer stunning views and a glimpse into Mayan history and culture.",
        place_image_url="/images/Mexico1_01.jpg",
        schedule_id=12
    )
    activity26 = Activity(
        place="SPER IK Lab",
        longitude=-87.4622,
        latitude=20.2079,
        description="Visit this contemporary art gallery set within a unique architectural space. The gallery features innovative exhibitions and installations that blend art with the natural environment.",
        place_image_url="/images/Mexico1_02.jpg",
        schedule_id=12
    )
    activity27 = Activity(
        place="Chichén Itzá",
        longitude=-88.5678,
        latitude=20.6829,
        description="Discover one of the New Seven Wonders of the World, an iconic archaeological site featuring the Pyramid of Kukulcán, the Temple of the Warriors, and the Great Ball Court.",
        place_image_url="/images/Mexico2_01.jpg",
        schedule_id=13
    )
    activity28 = Activity(
        place="Cenote Ik-Kil",
        longitude=-88.5504,
        latitude=20.6741,
        description="Swim in this beautiful open-air cenote located near Chichén Itzá. The cenote is surrounded by lush vegetation and offers crystal-clear waters perfect for a refreshing dip.",
        place_image_url="/images/Mexico2_02.webp",
        schedule_id=13
    )
    activity29 = Activity(
        place="Cenote Saamal",
        longitude=-88.5932,
        latitude=20.6900,
        description="Visit this picturesque cenote known for its stunning turquoise waters and cascading waterfall. It's a great spot for swimming and photography.",
        place_image_url="/images/Mexico2_03.webp",
        schedule_id=13
    )
    activity30 = Activity(
        place="Cenote Azul (Blue Cenote)",
        longitude=-87.2255,
        latitude=20.5450,
        description="Enjoy a relaxing day at this cenote, known for its clear blue waters and natural beauty. It's a popular spot for swimming, snorkeling, and diving.",
        place_image_url="/images/Mexico3_01.jpg",
        schedule_id=14
    )
    activity31 = Activity(
        place="Cenote Manatí",
        longitude=-87.4454,
        latitude=20.2439,
        description="Also known as Casa Cenote, this cenote offers a unique experience with its mix of freshwater and seawater. It's a great place for snorkeling and observing marine life.",
        place_image_url="/images/Mexico3_02.jpg",
        schedule_id=14
    )
    activity32 = Activity(
        place="XCaret",
        longitude=-87.4725,
        latitude=20.5784,
        description="Spend the day at this eco-archaeological park, which offers a mix of natural attractions, cultural performances, and adventure activities. Highlights include underground rivers, a coral reef aquarium, and a spectacular evening show.",
        place_image_url="/images/Mexico4_01.webp",
        schedule_id=15
    )
    activity33 = Activity(
        place="Playa Delfines",
        longitude=-86.7523,
        latitude=21.0467,
        description="Relax on this beautiful public beach known for its soft white sand and stunning turquoise waters. It's a great spot for sunbathing, swimming, and enjoying the ocean views.",
        place_image_url="/images/Mexico5_01.jpg",
        schedule_id=16
    )
    activity34 = Activity(
        place="Downtown",
        longitude=-86.8475,
        latitude=21.1619,
        description="Explore the vibrant downtown area of Cancun, where you can find local markets, restaurants, shops, and cultural attractions. It's a great place to experience the local culture and cuisine.",
        place_image_url="/images/Mexico5_02.jpg",
        schedule_id=16
    )
    activity35 = Activity(
        place="Isla Mujeres",
        longitude=-86.7447,
        latitude=21.2008,
        description="Take a ferry to this charming island located off the coast of Cancun. Enjoy its beautiful beaches, snorkeling spots, and laid-back atmosphere. Visit Punta Sur, Garrafon Natural Reef Park, and explore the island by golf cart or bicycle.",
        place_image_url="/images/Mexico6_01.webp",
        schedule_id=17
    )
    activity36 = Activity(
        place="Zion National Park",
        longitude=-113.0263,
        latitude=37.2982,
        description="The Canyon Overlook Trail is a short 1-mile round-trip hike that offers stunning views of Zion Canyon. The trail is moderate in difficulty and takes about 1 hour to complete. Lower Emerald Pool Trail is an easy 1.2-mile round-trip hike. The trail is family-friendly and offers beautiful views of the surrounding cliffs. You can extend the hike to the Upper Emerald Pools if you have more time.",
        place_image_url="/images/Utah1.jpg",
        schedule_id=18
    )
    activity37 = Activity(
        place="Monument Valley",
        longitude=-110.1116,
        latitude=36.9987,
        description="Start your day with a scenic drive to Monument Valley. The drive takes about 3 hours from Zion National Park, so plan to leave early.",
        place_image_url="/images/Utah1_02.jpg",
        schedule_id=19
    )
    activity38 = Activity(
        place="Forrest Gump Hill",
        longitude=-110.0833,
        latitude=37.1018,
        description="Upon arrival, visit the iconic Forrest Gump Hill, where the famous scene from the movie was filmed. Take some time to snap photos of the stunning landscape.",
        place_image_url="/images/Utah2.jpg",
        schedule_id=19
    )
    activity39 = Activity(
        place="Dead Horse Point State Park",
        longitude=-109.7394,
        latitude=38.4824,
        description="The Dead Horse Point Overlook Trail: Hike the Dead Horse Point Overlook Trail, a 1.5-mile loop that offers breathtaking views of the Colorado River and the surrounding canyons.",
        place_image_url="/images/Utah3_01.jpg",
        schedule_id=20
    )
    activity40 = Activity(
        place="Canyonlands National Park",
        longitude=-109.8214,
        latitude=38.3269,
        description="Start with a visit to Mesa Arch, a short 0.7-mile round-trip hike. The arch is particularly stunning at sunrise, but it’s beautiful at any time of day. Continue to the Grand View Point Overlook, where you can take a 2-mile round-trip hike along the rim of the canyon for panoramic views. End your day at the Green River Overlook, a viewpoint offering a spectacular view of the river winding through the canyon.",
        place_image_url="/images/Utah3_02.jpg",
        schedule_id=20
    )
    activity41 = Activity(
        place="Arches National Park",
        longitude=-109.5925,
        latitude=38.7331,
        description="Start your day early with a visit to Balanced Rock, an iconic formation in the park. It’s a short walk from the parking area. Then head to The Windows Section, where you can explore the North and South Windows, as well as Double Arch. This area is great for photography, especially in the early morning light. After lunch, hike to Delicate Arch, the most famous arch in the park. The hike is 3 miles round-trip and moderately challenging, with a steady incline and some rocky sections. The arch is best photographed in the late afternoon or early evening.",
        place_image_url="/images/Utah4.jpeg",
        schedule_id=21
    )
    activity42 = Activity(
        place="Capitol Reef National Park",
        longitude=-111.1681,
        latitude=38.2833,
        description="Start your day with a visit to Panorama Point for sweeping views of Capitol Reef’s colorful landscape. Then, head to The Castle, a prominent rock formation visible from the park’s main road. Visit the historic Fruita Schoolhouse to learn about the early settlers of the area. Then, stop by the Fremont Petroglyphs to see ancient rock art left by the Fremont people. End your day with a hike on the Hickman Bridge Trail, a 2-mile round-trip hike that takes you to a natural rock bridge. The hike is moderately challenging but offers great views along the way.",
        place_image_url="/images/Utah5.jpg",
        schedule_id=22
    )
    activity43 = Activity(
        place="Bryce Canyon National Park",
        longitude=-112.1871,
        latitude=37.5930,
        description="Start your day with a visit to Bryce Point for one of the best views of the Bryce Amphitheater. The early morning light creates a stunning contrast between the red rock hoodoos and the deep blue sky. Hike the Queen’s Garden Trail, a 1.8-mile round-trip trail that descends into the Bryce Amphitheater. This trail is often combined with the Navajo Loop Trail for a more comprehensive experience. End your trip with a sunset at Sunset Point. The hoodoos glow in the soft light, creating a perfect ending to your Utah adventure.",
        place_image_url="/images/Utah6.jpeg",
        schedule_id=23
    )
    activity44 = Activity(
        place="Carrizo Plain National Monument",
        longitude=-119.8099,
        latitude=35.0917,
        description="Start your day at Soda Lake, one of the largest alkaline lakes in California. The Soda Lake Overlook offers a great vantage point to see the expansive white salt flats. Take the short, easy trail to the overlook for panoramic views. Next, head to Painted Rock, a horseshoe-shaped sandstone formation with ancient pictographs created by the Chumash, Salinan, and Yokut tribes. You’ll need to check if guided tours are available, as access is sometimes restricted to protect the site. The hike to Painted Rock is about 2 miles round-trip. If you’re visiting in the spring, take some time to explore the wildflower fields that Carrizo Plain is famous for. The landscape transforms into a sea of vibrant colors, with blooms of goldfields, phacelia, and other native flowers. Popular spots for wildflower viewing include the eastern foothills of the Caliente Range and the Temblor Range.",
        place_image_url="/images/California1.jpeg",
        schedule_id=24
    )
    activity45 = Activity(
        place="Antelope Valley California Poppy Reserve State Natural Reserve",
        longitude=-118.3893,
        latitude=34.7268,
        description="Start your day early and drive to Antelope Valley California Poppy Reserve. The reserve is particularly stunning in the spring when the poppies are in full bloom. Aim to arrive early to beat the crowds and catch the flowers opening in the morning sunlight. Explore the various trails within the reserve. The South and North Poppy Loop Trails are popular and provide easy to moderate hikes with excellent views of the rolling hills covered in vibrant orange poppies. The entire loop is about 3.3 miles, but shorter sections can be done if preferred.",
        place_image_url="/images/California2.jpg",
        schedule_id=25
    )
    activity46 = Activity(
        place="San Francisco",
        longitude=-122.4194,
        latitude=37.7749,
        description="Start your trip in San Francisco. Consider spending some time exploring iconic spots like the Golden Gate Bridge, Fisherman’s Wharf, or Alcatraz Island if you haven’t already.",
        place_image_url="/images/CaliforniaHW1_01.webp",
        schedule_id=26
    )
    activity47 = Activity(
        place="Pacifica",
        longitude=-122.4869,
        latitude=37.6138,
        description="Begin your drive south on Highway 1. Stop in Pacifica for a quick hike along the Devil’s Slide Trail, a 1.3-mile paved trail with stunning ocean views.",
        place_image_url="/images/CaliforniaHW1_02.webp",
        schedule_id=26
    )
    activity48 = Activity(
        place="Half Moon Bay",
        longitude=-122.4286,
        latitude=37.4636,
        description="Continue to Half Moon Bay, known for its dramatic coastal cliffs and beaches. Visit the famous Mavericks Beach, where big wave surfing competitions are held. Enjoy lunch at a local seafood spot, then visit the nearby Fitzgerald Marine Reserve to explore tide pools.",
        place_image_url="/images/CaliforniaHW1_03.jpg",
        schedule_id=26
    )
    activity49 = Activity(
        place="Santa Cruz",
        longitude=-122.0308,
        latitude=36.9741,
        description="Arrive in Santa Cruz and check into your accommodations. Spend the evening strolling along the Santa Cruz Beach Boardwalk, one of California’s last remaining seaside amusement parks. Enjoy dinner at a local restaurant and take in the lively atmosphere.",
        place_image_url="/images/CaliforniaHW1_04.jpg",
        schedule_id=26
    )
    activity50 = Activity(
        place="Monterey",
        longitude=-121.8947,
        latitude=36.6002,
        description="Drive south to Monterey, home to the world-renowned Monterey Bay Aquarium. Spend the morning exploring the aquarium or take a scenic drive along 17-Mile Drive, which offers incredible views of the Pacific Ocean, Pebble Beach, and the famous Lone Cypress.",
        place_image_url="/images/CaliforniaHW2_01.jpeg",
        schedule_id=27
    )
    activity51 = Activity(
        place="Carmel-by-the-Sea",
        longitude=-121.9233,
        latitude=36.5552,
        description="Continue to Carmel-by-the-Sea, a charming town known for its art galleries and fairy-tale cottages. Take a walk along Carmel Beach, visit the historic Carmel Mission, or explore the shops and galleries in town. Enjoy lunch at one of Carmel’s many cozy cafes.",
        place_image_url="/images/CaliforniaHW2_01.jpg",
        schedule_id=27
    )
    activity52 = Activity(
        place="Big Sur",
        longitude=-121.8058,
        latitude=36.2704,
        description="Drive into Big Sur, one of the most beautiful stretches of coastline in the world. Stop at Bixby Creek Bridge for a photo op and continue to your accommodations. Big Sur offers various options, from rustic cabins to luxury resorts. Spend the evening enjoying the tranquility of the area.",
        place_image_url="/images/CaliforniaHW2_02.jpg",
        schedule_id=27
    )
    activity53 = Activity(
        place="Julia Pfeiffer Burns State Park",
        longitude=-121.6705,
        latitude=36.1584,
        description="Start your day with a visit to Julia Pfeiffer Burns State Park. Hike the McWay Falls Trail, a short and easy hike that leads to a viewpoint overlooking an 80-foot waterfall cascading onto the beach. This is one of Big Sur’s most iconic sights.",
        place_image_url="/images/CaliforniaHW3_01.jpg",
        schedule_id=28
    )
    activity54 = Activity(
        place="Pfeiffer Beach",
        longitude=-121.7990,
        latitude=36.2383,
        description="Head to Pfeiffer Beach, known for its purple sand and unique rock formations. The beach is somewhat hidden, so keep an eye out for the narrow road leading to the parking area. Spend some time exploring the beach and taking in the stunning scenery.",
        place_image_url="/images/CaliforniaHW3_02.jpg",
        schedule_id=28
    )
    activity55 = Activity(
        place="Ventana Wilderness",
        longitude=-121.6597,
        latitude=36.2405,
        description="If you’re up for more adventure, consider a hike in the Ventana Wilderness. The Ewoldsen Trail is a moderately challenging hike that offers fantastic views of the Big Sur coastline and redwood forests.",
        place_image_url="/images/CaliforniaHW3_03.jpg",
        schedule_id=28
    )
    activity56 = Activity(
        place="Hearst Castle",
        longitude=-121.1664,
        latitude=35.6852,
        description="Drive south to San Simeon and visit Hearst Castle, the opulent estate of newspaper magnate William Randolph Hearst. Take a guided tour of the mansion and its beautiful gardens. The views of the coast from the castle are spectacular.",
        place_image_url="/images/CaliforniaHW4_01.jpg",
        schedule_id=29
    )
    activity57 = Activity(
        place="Elephant Seal Rookery",
        longitude=-121.2837,
        latitude=35.6652,
        description="Just a short drive south of Hearst Castle, stop at the Elephant Seal Rookery at Piedras Blancas. Depending on the time of year, you can see hundreds of elephant seals lounging on the beach, an unforgettable wildlife experience.",
        place_image_url="/images/CaliforniaHW4_02.jpg",
        schedule_id=29
    )
    activity58 = Activity(
        place="Cambria",
        longitude=-121.0814,
        latitude=35.5641,
        description="Continue to the charming town of Cambria. Take a stroll through the town’s quaint shops and art galleries or visit Moonstone Beach for a walk along the boardwalk. Enjoy lunch at a local café before continuing your journey.",
        place_image_url="/images/CaliforniaHW4_03.png",
        schedule_id=29
    )
    activity59 = Activity(
        place="San Luis Obispo",
        longitude=-120.6602,
        latitude=35.2828,
        description="Arrive in San Luis Obispo, often called the “Happiest City in America.” Explore the downtown area, visit Mission San Luis Obispo de Tolosa, and enjoy a farm-to-table dinner at one of the city’s excellent restaurants.",
        place_image_url="/images/CaliforniaHW4_04.jpg",
        schedule_id=29
    )
    activity60 = Activity(
        place="Pismo Beach",
        longitude=-120.6464,
        latitude=35.1428,
        description="Start your day with a visit to Pismo Beach, known for its wide sandy beaches and iconic pier. If you’re visiting in the right season, you can also stop by the Monarch Butterfly Grove to see thousands of butterflies clustered in the trees.",
        place_image_url="/images/CaliforniaHW5_01.jpeg",
        schedule_id=30
    )
    activity61 = Activity(
        place="Solvang",
        longitude=-120.1376,
        latitude=34.5958,
        description="Continue south to Solvang, a charming Danish-style town in the Santa Ynez Valley. Explore the town’s unique architecture, visit a few of the many bakeries for authentic Danish pastries, and consider a quick visit to a local winery for a tasting.",
        place_image_url="/images/CaliforniaHW5_04.jpg",
        schedule_id=30
    )
    activity62 = Activity(
        place="Santa Barbara",
        longitude=-119.6982,
        latitude=34.4208,
        description="Arrive in Santa Barbara, a city known for its Mediterranean-style architecture and beautiful beaches. Visit the historic Santa Barbara Mission, stroll along State Street for shopping and dining, and relax at the waterfront or on one of the city’s many beaches.",
        place_image_url="/images/CaliforniaHW5_02.jpg",
        schedule_id=30
    )
    activity63 = Activity(
        place="Stearns Wharf",
        longitude=-119.6885,
        latitude=34.4105,
        description="End your trip with a sunset at Stearns Wharf, where you can enjoy views of the coastline and the Santa Ynez Mountains. Enjoy dinner at one of the waterfront restaurants and reflect on the incredible journey along Highway 1.",
        place_image_url="/images/CaliforniaHW5_03.jpg",
        schedule_id=30
    )
    activity64 = Activity(
        place="Diamond Head",
        longitude=-157.8058,
        latitude=21.2620,
        description="A must-visit landmark! This trail is perfect for all ages to hike together. At the summit, enjoy panoramic views of Waikiki Beach and the Pacific Ocean's stunning blue waters.",
        place_image_url="/images/Hawaii1_01.webp",
        schedule_id=31
    )
    activity65 = Activity(
        place="Island Vintage Coffee",
        longitude=-157.8286,
        latitude=21.2803,
        description="A popular spot near the hotel known for its Acai bowls, grilled shrimp rice, and the best Loco Moco. Be prepared for long lines, but you can order for pickup from the wine bar.",
        place_image_url="/images/Hawaii1_02.webp",
        schedule_id=31
    )
    activity66 = Activity(
        place="Lanikai Beach",
        longitude=-157.7145,
        latitude=21.3931,
        description="Known as 'Oahu's most beautiful beach' and 'Hawaii's best beach' by multiple organizations, this spot offers a serene and stunning beach experience.",
        place_image_url="/images/Hawaii1_03.jpg",
        schedule_id=31
    )
    activity67 = Activity(
        place="Ginza Bairin Tonkatsu & Yoshoku",
        longitude=-157.8287,
        latitude=21.2793,
        description="Renowned for its specialty thick-cut pork loin katsu.",
        place_image_url="/images/Hawaii1_04.jpg",
        schedule_id=31
    )
    activity68 = Activity(
        place="Dole Plantation",
        longitude=-158.0318,
        latitude=21.5240,
        description="Take a two-mile, 20-minute narrated train ride through a working plantation and explore eight different gardens. A great educational and fun experience for the whole family.",
        place_image_url="/images/Hawaii2_01.avif",
        schedule_id=32
    )
    activity69 = Activity(
        place="Laniakea Beach",
        longitude=-158.1056,
        latitude=21.5958,
        description="Famous for its turtle sightings, this beach offers a nearly guaranteed chance to see turtles landing on the shore between 12:00 PM and 3:30 PM.",
        place_image_url="/images/Hawaii2_02.jpg",
        schedule_id=32
    )
    activity70 = Activity(
        place="Sunset Beach Park",
        longitude=-158.0491,
        latitude=21.6751,
        description="Home to a famous hundred-year-old coconut tree that grows horizontally. A beautiful place to relax and enjoy the sunset.",
        place_image_url="/images/Hawaii2_03.webp",
        schedule_id=32
    )
    activity71 = Activity(
        place="Pearl Harbor National Memorial",
        longitude=-157.9378,
        latitude=21.3647,
        description="Visit the USS Arizona Memorial and take a guided tour of the Battleship Missouri. Experience a piece of history that honors those who lost their lives in the attack on Pearl Harbor.",
        place_image_url="/images/Hawaii3_01.jpg",
        schedule_id=33
    )
    activity72 = Activity(
        place="Hanauma Bay Snorkeling",
        longitude=-157.6935,
        latitude=21.2690,
        description="Experience snorkeling in one of Hawaii’s most famous and beautiful nature preserves. Hanauma Bay offers crystal clear waters and a vibrant coral reef filled with marine life, making it an ideal spot for both beginners and experienced snorkelers.",
        place_image_url="/images/Hawaii3_02.jpg",
        schedule_id=33
    )
    activity73 = Activity(
        place="Kualoa Ranch",
        longitude=-157.8374,
        latitude=21.5216,
        description="Take the 'Hawaii’s Best Movie Tour' and explore famous filming locations for a fun and interactive experience.",
        place_image_url="/images/Hawaii4.jpg",
        schedule_id=34
    )
    activity74 = Activity(
        place="Polynesian Cultural Center",
        longitude=-157.9238,
        latitude=21.6387,
        description="Enjoy a group guided tour through six authentic island villages, a delicious Alii Luau buffet, and the 'HA: Breath of Life' show. A perfect way to experience Polynesian culture.",
        place_image_url="/images/Hawaii5.jpg",
        schedule_id=35
    )
    activity75 = Activity(
        place="Duquesne Incline",
        longitude=-80.0125,
        latitude=40.4314,
        description="Ride the historic incline for panoramic views of the Pittsburgh skyline.",
        place_image_url="/images/Pittsburgh1_01.webp",
        schedule_id=36
    )
    activity76 = Activity(
        place="Mt. Washington Overlook",
        longitude=-80.0110,
        latitude=40.4284,
        description="A scenic overlook offering stunning views of downtown Pittsburgh and its surrounding rivers.",
        place_image_url="/images/Pittsburgh1_02.jpg",
        schedule_id=36
    )
    activity77 = Activity(
        place="First Watch",
        longitude=-79.9939,
        latitude=40.4375,
        description="A popular brunch spot known for its delicious breakfast and lunch options.",
        place_image_url="/images/Pittsburgh2_01.jpeg",
        schedule_id=37
    )
    activity78 = Activity(
        place="Cathedral of Learning",
        longitude=-79.9532,
        latitude=40.4442,
        description="Visit the iconic Cathedral of Learning at the University of Pittsburgh, known for its impressive architecture.",
        place_image_url="/images/Pittsburgh2_02.webp",
        schedule_id=37
    )
    activity79 = Activity(
        place="Carnegie Museum of Art",
        longitude=-79.9508,
        latitude=40.4431,
        description="Visit this renowned museum to explore a wide array of art collections, from classic to contemporary.",
        place_image_url="/images/Pittsburgh2_03.avif",
        schedule_id=37
    )
    activity80 = Activity(
        place="Aladin Show",
        longitude=-79.9961,
        latitude=40.4406,
        description="End your day with a captivating performance at Aladin, with tickets reserved for 6:30 PM.",
        place_image_url="/images/Pittsburgh2_04.webp",
        schedule_id=37
    )
    activity81 = Activity(
        place="Fallingwater",
        longitude=-79.4685,
        latitude=39.9066,
        description="Tour Frank Lloyd Wright’s famous architectural masterpiece.",
        place_image_url="/images/Pittsburgh3_01.jpg",
        schedule_id=38
    )
    activity82 = Activity(
        place="Flight 93 National Memorial",
        longitude=-78.8986,
        latitude=40.0520,
        description="Visit the 9/11 memorial dedicated to the heroes of Flight 93, located about 1 hour from Fallingwater.",
        place_image_url="/images/Pittsburgh3_02.jpg",
        schedule_id=38
    )
    activity83 = Activity(
        place="Botanic Garden",
        longitude=-80.0186,
        latitude=40.4414,
        description="Stroll through beautiful gardens at the Botanic Garden. Open from 9:30 a.m. to 5 p.m.",
        place_image_url="/images/Pittsburgh4_01.jpg",
        schedule_id=39
    )
    activity84 = Activity(
        place="Carnegie Mellon University",
        longitude=-79.9435,
        latitude=40.4435,
        description="Explore the beautiful campus of Carnegie Mellon University, renowned for its cutting-edge research and prestigious academic programs. Stroll through the scenic walkways, admire the modern architecture, and visit key landmarks like the Gates Center for Computer Science.",
        place_image_url="/images/Pittsburgh4_02.jpg",
        schedule_id=39
    )
    activity85 = Activity(
        place="Giant Forest Museum",
        longitude=-118.7720,
        latitude=36.5616,
        description="Learn about the giant sequoias and the park's history at the Giant Forest Museum. Explore exhibits that provide insight into the ecology and preservation efforts of Sequoia National Park.",
        place_image_url="/images/Tree1_01.jpg",
        schedule_id=40
    )
    activity86 = Activity(
        place="General Sherman Tree",
        longitude=-118.7511,
        latitude=36.5819,
        description="Visit the General Sherman Tree, the largest living tree by volume. This iconic sequoia stands over 275 feet tall and offers a short hiking trail from the parking area to view this natural wonder.",
        place_image_url="/images/Tree1_02.jpg",
        schedule_id=40
    )
    activity87 = Activity(
        place="Moro Rock",
        longitude=-118.7657,
        latitude=36.5451,
        description="Climb the stairway to the top of Moro Rock for panoramic views of the Sierra Nevada mountains. The climb involves over 350 steps but rewards visitors with breathtaking vistas from the summit.",
        place_image_url="/images/Tree1_03.jpg",
        schedule_id=40
    )
    activity88 = Activity(
        place="General Grant Tree",
        longitude=-118.9721,
        latitude=36.7470,
        description="Visit the General Grant Tree in Kings Canyon National Park, known as the Nation’s Christmas Tree. This is the second-largest tree in the world and a highlight of the park.",
        place_image_url="/images/Tree2_01.jpg",
        schedule_id=41
    )
    activity89 = Activity(
        place="Kings Canyon Scenic Byway",
        longitude=-118.5905,
        latitude=36.8028,
        description="Drive along the Kings Canyon Scenic Byway to experience one of California’s most beautiful scenic drives. Enjoy dramatic landscapes, including towering cliffs, deep canyons, and lush forests.",
        place_image_url="/images/Tree2_02.jpg",
        schedule_id=41
    )
    activity90 = Activity(
        place="Hollywood Walk of Fame",
        longitude=-118.3257,
        latitude=34.1015,
        description="Walk along the famous Hollywood Walk of Fame, where you'll find the stars of your favorite celebrities embedded in the sidewalk.",
        place_image_url="/images/LA1_01.jpg",
        schedule_id=42
    )
    activity91 = Activity(
        place="Griffith Observatory",
        longitude=-118.3004,
        latitude=34.1184,
        description="Visit the Griffith Observatory for panoramic views of Los Angeles and the iconic Hollywood sign. Explore the exhibits and enjoy stargazing in the evening.",
        place_image_url="/images/LA1_02.jpg",
        schedule_id=42
    )
    activity92 = Activity(
        place="The Getty Center",
        longitude=-118.4738,
        latitude=34.0780,
        description="Explore The Getty Center, known for its impressive architecture, gardens, and a vast collection of European paintings and sculptures.",
        place_image_url="/images/LA1_03.jpg",
        schedule_id=42
    )
    activity93 = Activity(
        place="Santa Monica Pier",
        longitude=-118.4954,
        latitude=34.0104,
        description="Spend time at the Santa Monica Pier, featuring an amusement park, aquarium, and numerous dining options. Don't forget to walk along the beach.",
        place_image_url="/images/LA2_01.jpg",
        schedule_id=43
    )
    activity94 = Activity(
        place="Venice Beach",
        longitude=-118.4722,
        latitude=33.9850,
        description="Visit Venice Beach, known for its lively boardwalk, street performers, Muscle Beach gym, and skate park. Great for people-watching and relaxing by the sea.",
        place_image_url="/images/LA2_02.webp",
        schedule_id=43
    )
    activity95 = Activity(
        place="Los Angeles County Museum of Art (LACMA)",
        longitude=-118.3595,
        latitude=34.0625,
        description="Explore LACMA, the largest art museum in the western United States, featuring a diverse collection of contemporary and historical art pieces.",
        place_image_url="/images/LA2_03.jpeg",
        schedule_id=43
    )
    activity96 = Activity(
        place="Central Park",
        longitude=-73.9654,
        latitude=40.7829,
        description="Relax and explore the vast green spaces of Central Park. Rent a bike, enjoy a picnic, or visit the Central Park Zoo.",
        place_image_url="/images/NY1_01.webp",
        schedule_id=44
    )
    activity97 = Activity(
        place="Times Square",
        longitude=-73.9851,
        latitude=40.7580,
        description="Experience the dazzling lights and bustling energy of Times Square. Visit the numerous shops, theaters, and iconic landmarks.",
        place_image_url="/images/NY1_02.jpg",
        schedule_id=44
    )
    activity98 = Activity(
        place="Top of the Rock Observation Deck",
        longitude=-73.9787,
        latitude=40.7590,
        description="Visit the Top of the Rock Observation Deck at Rockefeller Center for stunning panoramic views of New York City, including the Empire State Building.",
        place_image_url="/images/NY1_03.jpg",
        schedule_id=44
    )
    activity99 = Activity(
        place="Statue of Liberty",
        longitude=-74.0445,
        latitude=40.6892,
        description="Take a ferry to Liberty Island and visit the iconic Statue of Liberty. Learn about its history and significance at the museum on the island.",
        place_image_url="/images/NY2_01.jpg",
        schedule_id=45
    )
    activity100 = Activity(
        place="Ellis Island",
        longitude=-74.0423,
        latitude=40.6995,
        description="Explore Ellis Island, once the busiest immigrant inspection station in the United States, and learn about its role in America's immigration history.",
        place_image_url="/images/NY2_02.jpg",
        schedule_id=45
    )
    activity101 = Activity(
        place="Broadway Show",
        longitude=-73.9862,
        latitude=40.7590,
        description="End your day with a Broadway show. Choose from a wide range of performances, from classic musicals to contemporary dramas.",
        place_image_url="/images/NY2_03.jpeg",
        schedule_id=45
    )
    activity102 = Activity(
        place="Freedom Trail",
        longitude=-71.0603,
        latitude=42.3550,
        description="Walk the historic Freedom Trail, a 2.5-mile route that takes you through 16 significant historical sites, including Paul Revere's House and the Old North Church.",
        place_image_url="/images/Boston1_01.JPG",
        schedule_id=46
    )
    activity103 = Activity(
        place="Boston Public Garden",
        longitude=-71.0690,
        latitude=42.3545,
        description="Visit the beautiful Boston Public Garden, America's first public botanical garden. Enjoy a ride on the famous Swan Boats.",
        place_image_url="/images/Boston1_02.jpg",
        schedule_id=46
    )
    activity104 = Activity(
        place="Quincy Market",
        longitude=-71.0551,
        latitude=42.3607,
        description="Explore Quincy Market, a historic marketplace offering a variety of food stalls, shops, and entertainment. A great place to grab lunch and enjoy the lively atmosphere.",
        place_image_url="/images/Boston1_03.jpg",
        schedule_id=46
    )
    activity105 = Activity(
        place="Harvard University Tour",
        longitude=-71.1167,
        latitude=42.3770,
        description="Take a guided tour of Harvard University, the oldest institution of higher education in the United States. Explore the historic campus and its notable landmarks.",
        place_image_url="/images/Boston2_01.jpg",
        schedule_id=47
    )
    activity106 = Activity(
        place="Museum of Fine Arts, Boston",
        longitude=-71.0934,
        latitude=42.3394,
        description="Visit the Museum of Fine Arts, Boston, known for its extensive collection of artworks from around the world, spanning centuries of history and culture.",
        place_image_url="/images/Boston2_02.jpg",
        schedule_id=47
    )
    activity107 = Activity(
        place="Fenway Park",
        longitude=-71.0972,
        latitude=42.3467,
        description="Tour Fenway Park, the historic home of the Boston Red Sox. Learn about the park's storied history and catch a game if the team is in town.",
        place_image_url="/images/Boston2_03.jpg",
        schedule_id=47
    )
    activity108 = Activity(
        place="Yosemite Valley",
        longitude=-119.5936,
        latitude=37.7456,
        description="Explore Yosemite Valley, the heart of the park, surrounded by towering cliffs, waterfalls, and famous landmarks like El Capitan and Half Dome.",
        place_image_url="/images/Yosemite1_01.webp",
        schedule_id=48
    )
    activity109 = Activity(
        place="Yosemite Falls",
        longitude=-119.5967,
        latitude=37.7554,
        description="Hike to Yosemite Falls, one of the tallest waterfalls in North America, with a total drop of 2,425 feet. The views are spectacular, especially in the spring.",
        place_image_url="/images/Yosemite1_02.jpg",
        schedule_id=48
    )
    activity110 = Activity(
        place="Glacier Point",
        longitude=-119.5742,
        latitude=37.7302,
        description="Drive or hike to Glacier Point, an iconic viewpoint offering breathtaking panoramic views of Yosemite Valley, Half Dome, and the High Sierra.",
        place_image_url="/images/Yosemite1_03.jpg",
        schedule_id=48
    )
    activity111 = Activity(
        place="Mariposa Grove",
        longitude=-119.6021,
        latitude=37.5039,
        description="Visit Mariposa Grove, home to over 500 mature giant sequoias, some of the largest and oldest trees on Earth. Take a hike among these ancient giants.",
        place_image_url="/images/Yosemite2_01.jpg",
        schedule_id=49
    )
    activity112 = Activity(
        place="Bridalveil Fall",
        longitude=-119.6465,
        latitude=37.7176,
        description="Stop at Bridalveil Fall, a 620-foot waterfall that flows year-round. The trail to the base is short and easy, offering a close-up view of the falls.",
        place_image_url="/images/Yosemite2_02.jpg",
        schedule_id=49
    )
    activity113 = Activity(
        place="Tuolumne Meadows",
        longitude=-119.3246,
        latitude=37.8748,
        description="Explore Tuolumne Meadows, a high-altitude meadow area known for its stunning alpine scenery, hiking trails, and opportunities for wildlife viewing.",
        place_image_url="/images/Yosemite2_03.jpg",
        schedule_id=49
    )
    activity114 = Activity(
        place="French Quarter",
        longitude=-90.0659,
        latitude=29.9584,
        description="Wander through the historic French Quarter, known for its vibrant nightlife, music, and unique architecture. Visit Jackson Square and the St. Louis Cathedral.",
        place_image_url="/images/NO1_01.jpg",
        schedule_id=50
    )
    activity115 = Activity(
        place="Bourbon Street",
        longitude=-90.0686,
        latitude=29.9589,
        description="Experience the lively atmosphere of Bourbon Street, with its array of bars, restaurants, and music venues showcasing New Orleans' rich jazz culture.",
        place_image_url="/images/NO1_02.jpg",
        schedule_id=50
    )
    activity116 = Activity(
        place="Frenchmen Street",
        longitude=-90.0568,
        latitude=29.9636,
        description="Head to Frenchmen Street for live jazz music, art markets, and some of the best local eateries. It's a must-visit for any music lover.",
        place_image_url="/images/NO1_03.jpg",
        schedule_id=50
    )
    activity117 = Activity(
        place="Garden District",
        longitude=-90.0807,
        latitude=29.9275,
        description="Take a stroll through the Garden District, known for its historic mansions, tree-lined streets, and charming boutiques. Don't miss Lafayette Cemetery No. 1.",
        place_image_url="/images/NO2_01.jpg",
        schedule_id=51
    )
    activity118 = Activity(
        place="National WWII Museum",
        longitude=-90.0702,
        latitude=29.9434,
        description="Visit the National WWII Museum, one of the most comprehensive WWII museums in the world, offering immersive exhibits and personal stories from the war.",
        place_image_url="/images/NO2_02.jpg",
        schedule_id=51
    )
    activity119 = Activity(
        place="Audubon Park",
        longitude=-90.1306,
        latitude=29.9225,
        description="Relax at Audubon Park, a beautiful urban park with walking trails, a lagoon, and the Audubon Zoo. It's a great spot to unwind and enjoy nature.",
        place_image_url="/images/NO2_03.jpg",
        schedule_id=51
    )
    activity120 = Activity(
        place="Duval Street",
        longitude=-81.8029,
        latitude=24.5552,
        description="Stroll along Duval Street, Key West's main thoroughfare, known for its lively atmosphere, shops, and historic bars.",
        place_image_url="/images/KeyWest1_01.jpg",
        schedule_id=52
    )
    activity121 = Activity(
        place="Hemingway Home and Museum",
        longitude=-81.8016,
        latitude=24.5515,
        description="Visit the former home of author Ernest Hemingway, now a museum showcasing his life and work. Don't miss the famous six-toed cats that reside here.",
        place_image_url="/images/KeyWest1_02.jpeg",
        schedule_id=52
    )
    activity122 = Activity(
        place="Southernmost Point Buoy",
        longitude=-81.8035,
        latitude=24.5465,
        description="Take a photo at the Southernmost Point Buoy, a popular landmark marking the southernmost tip of the continental United States.",
        place_image_url="/images/KeyWest1_03.jpg",
        schedule_id=52
    )
    activity123 = Activity(
        place="Key West Butterfly & Nature Conservatory",
        longitude=-81.8005,
        latitude=24.5473,
        description="Walk among hundreds of free-flying butterflies and exotic birds in this beautiful conservatory. It's a serene and colorful experience.",
        place_image_url="/images/KeyWest2_01.webp",
        schedule_id=53
    )
    activity124 = Activity(
        place="Mallory Square",
        longitude=-81.8087,
        latitude=24.5604,
        description="Join the sunset celebration at Mallory Square, where street performers, food vendors, and artists gather to create a lively atmosphere.",
        place_image_url="/images/KeyWest2_02.jpg",
        schedule_id=53
    )
    activity125 = Activity(
        place="Fort Zachary Taylor Historic State Park",
        longitude=-81.8092,
        latitude=24.5484,
        description="Explore Fort Zachary Taylor, a historic Civil War-era fort, and enjoy the park's beautiful beach, which is perfect for swimming and snorkeling.",
        place_image_url="/images/KeyWest2_03.jpg",
        schedule_id=53
    )
    activity126 = Activity(
        place="Hidden Valley Nature Trail",
        longitude=-116.1590,
        latitude=34.0128,
        description="Hike the Hidden Valley Nature Trail, a 1-mile loop trail that offers stunning rock formations and the chance to spot native wildlife.",
        place_image_url="/images/JoshuaTree1_01.jpg",
        schedule_id=54
    )
    activity127 = Activity(
        place="Skull Rock",
        longitude=-116.1031,
        latitude=34.0252,
        description="Visit Skull Rock, a unique rock formation resembling a human skull. The surrounding area offers great photo opportunities and short trails.",
        place_image_url="/images/JoshuaTree1_02.jpg",
        schedule_id=54
    )
    activity128 = Activity(
        place="Cholla Cactus Garden",
        longitude=-115.9220,
        latitude=33.9146,
        description="Explore the Cholla Cactus Garden, a dense collection of cholla cacti that glow in the sunlight, offering a beautiful desert landscape.",
        place_image_url="/images/JoshuaTree1_03.webp",
        schedule_id=54
    )
    activity129 = Activity(
        place="Zabriskie Point",
        longitude=-116.8105,
        latitude=36.4207,
        description="Watch the sunrise at Zabriskie Point, a famous viewpoint offering panoramic views of the badlands and rugged desert landscapes.",
        place_image_url="/images/DeathValley2_01.jpg",
        schedule_id=55
    )
    activity130 = Activity(
        place="Mesquite Flat Sand Dunes",
        longitude=-116.7052,
        latitude=36.6198,
        description="Visit Mesquite Flat Sand Dunes, where you can hike among the dunes, watch the sunset, and experience the vastness of Death Valley's desert.",
        place_image_url="/images/DeathValley2_02.jpg",
        schedule_id=55
    )
    activity131 = Activity(
        place="Dante's View",
        longitude=-116.7310,
        latitude=36.2285,
        description="Drive to Dante's View, a viewpoint located high above the valley floor, offering breathtaking views of the Panamint Range and Badwater Basin.",
        place_image_url="/images/DeathValley2_03.jpg",
        schedule_id=55
    )
    activity132 = Activity(
        place="Artist's Drive",
        longitude=-116.7677,
        latitude=36.3625,
        description="Take a scenic drive along Artist's Drive, a 9-mile loop that features colorful hills and the famous Artist's Palette formation.",
        place_image_url="/images/DeathValley3_01.jpg",
        schedule_id=56
    )
    activity133 = Activity(
        place="Badwater Basin",
        longitude=-116.8258,
        latitude=36.2403,
        description="Visit Badwater Basin, the lowest point in North America at 282 feet below sea level. The salt flats stretch for miles, creating a surreal landscape.",
        place_image_url="/images/DeathValley3_02.jpg",
        schedule_id=56
    )
    activity134 = Activity(
        place="Golden Canyon",
        longitude=-116.7385,
        latitude=36.4202,
        description="Hike Golden Canyon, a popular trail that takes you through colorful canyons and leads to Red Cathedral, a stunning rock formation.",
        place_image_url="/images/DeathValley3_03.webp",
        schedule_id=56
    )
    activity135 = Activity(
        place="Emerald Bay State Park",
        longitude=-120.1016,
        latitude=38.9494,
        description="Visit Emerald Bay State Park, known for its stunning views of the bay, hiking trails, and the historic Vikingsholm castle.",
        place_image_url="/images/Tahoe1_01.webp",
        schedule_id=57
    )
    activity136 = Activity(
        place="Sand Harbor Beach",
        longitude=-119.9401,
        latitude=39.1979,
        description="Relax at Sand Harbor Beach, one of Lake Tahoe's most beautiful spots, known for its clear turquoise waters and scenic boulder formations.",
        place_image_url="/images/Tahoe1_02.jpg",
        schedule_id=57
    )
    activity137 = Activity(
        place="Heavenly Gondola Ride",
        longitude=-119.9234,
        latitude=38.9576,
        description="Take the Heavenly Gondola for breathtaking panoramic views of Lake Tahoe and the surrounding mountains. The observation deck offers stunning photo opportunities.",
        place_image_url="/images/Tahoe1_03.jpg",
        schedule_id=57
    )
    activity138 = Activity(
        place="Donner Memorial State Park",
        longitude=-120.2288,
        latitude=39.3235,
        description="Visit Donner Memorial State Park, where you can learn about the history of the Donner Party and explore scenic trails around Donner Lake.",
        place_image_url="/images/Tahoe2_01.jpeg",
        schedule_id=58
    )
    activity139 = Activity(
        place="Kings Beach State Recreation Area",
        longitude=-120.0339,
        latitude=39.2378,
        description="Spend time at Kings Beach, a popular spot for swimming, sunbathing, and water sports. The beach offers beautiful views and a laid-back atmosphere.",
        place_image_url="/images/Tahoe2_02.webp",
        schedule_id=58
    )
    activity140 = Activity(
        place="Truckee River Rafting",
        longitude=-120.1843,
        latitude=39.3080,
        description="Experience the thrill of rafting on the Truckee River. This family-friendly activity offers scenic views and a fun adventure on the water.",
        place_image_url="/images/Tahoe2_03.jpg",
        schedule_id=58
    )
    activity141 = Activity(
        place="CN Tower",
        longitude=-79.3871,
        latitude=43.6426,
        description="Visit the iconic CN Tower, one of the tallest structures in the world. Take an elevator ride to the observation deck for breathtaking views of Toronto.",
        place_image_url="/images/Toronto1_01.webp",
        schedule_id=59
    )

    activity142 = Activity(
        place="Ripley's Aquarium of Canada",
        longitude=-79.3850,
        latitude=43.6424,
        description="Explore Ripley's Aquarium, home to over 20,000 marine animals. Walk through the underwater tunnel and marvel at sharks, rays, and vibrant coral reefs.",
        place_image_url="/images/Toronto1_02.jpeg",
        schedule_id=59
    )
    activity143 = Activity(
        place="Distillery District",
        longitude=-79.3598,
        latitude=43.6503,
        description="Explore the historic Distillery District, known for its cobblestone streets, art galleries, boutiques, and trendy restaurants.",
        place_image_url="/images/Toronto1_03.jpg",
        schedule_id=59
    )
    activity144 = Activity(
        place="Royal Ontario Museum",
        longitude=-79.3948,
        latitude=43.6677,
        description="Visit the Royal Ontario Museum, Canada's largest museum, featuring exhibits on natural history, world cultures, and art. Don't miss the dinosaur gallery.",
        place_image_url="/images/Toronto2_01.webp",
        schedule_id=60
    )

    activity145 = Activity(
        place="Toronto Islands",
        longitude=-79.3775,
        latitude=43.6238,
        description="Take a ferry to the Toronto Islands, offering beautiful parks, beaches, and recreational activities. Enjoy cycling, picnicking, and skyline views.",
        place_image_url="/images/Toronto2_02.jpg",
        schedule_id=60
    )
    activity146 = Activity(
        place="Kensington Market",
        longitude=-79.4005,
        latitude=43.6541,
        description="Wander through Kensington Market, a vibrant neighborhood known for its eclectic shops, diverse food scene, and colorful street art.",
        place_image_url="/images/Toronto2_03.jpg",
        schedule_id=60
    )
    activity147 = Activity(
        place="Window of the World",
        longitude=113.9736,
        latitude=22.5386,
        description="Explore Window of the World, a theme park that features miniature replicas of famous landmarks from around the world.",
        place_image_url="/images/Shenzhen1_01.jpg",
        schedule_id=61
    )
    activity148 = Activity(
        place="OCT Loft Creative Culture Park",
        longitude=113.9712,
        latitude=22.5446,
        description="Visit OCT Loft Creative Culture Park, a cultural and art district known for its galleries, cafes, and creative spaces.",
        place_image_url="/images/Shenzhen1_02.jpg",
        schedule_id=61
    )
    activity149 = Activity(
        place="Splendid China Folk Village",
        longitude=113.9813,
        latitude=22.5360,
        description="Discover Splendid China Folk Village, showcasing China's diverse culture and history through miniatures of famous landmarks and live performances.",
        place_image_url="/images/Shenzhen1_03.jpg",
        schedule_id=61
    )
    activity150 = Activity(
        place="Shenzhen Museum",
        longitude=114.0646,
        latitude=22.5474,
        description="Learn about Shenzhen's rapid development and history at the Shenzhen Museum, featuring exhibits on the city's transformation and cultural heritage.",
        place_image_url="/images/Shenzhen2_01.jpg",
        schedule_id=62
    )
    activity151 = Activity(
        place="Nanshan Mountains",
        longitude=113.9295,
        latitude=22.5329,
        description="Hike up Nanshan Mountain for panoramic views of Shenzhen's skyline and the South China Sea. The trail offers a peaceful retreat from the city.",
        place_image_url="/images/Shenzhen2_02.jpg",
        schedule_id=62
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
    db.session.add(activity64)
    db.session.add(activity65)
    db.session.add(activity66)
    db.session.add(activity67)
    db.session.add(activity68)
    db.session.add(activity69)
    db.session.add(activity70)
    db.session.add(activity71)
    db.session.add(activity72)
    db.session.add(activity73)
    db.session.add(activity74)
    db.session.add(activity75)
    db.session.add(activity76)
    db.session.add(activity77)
    db.session.add(activity78)
    db.session.add(activity79)
    db.session.add(activity80)
    db.session.add(activity81)
    db.session.add(activity82)
    db.session.add(activity83)
    db.session.add(activity84)
    db.session.add(activity85)
    db.session.add(activity86)
    db.session.add(activity87)
    db.session.add(activity88)
    db.session.add(activity89)
    db.session.add(activity90)
    db.session.add(activity91)
    db.session.add(activity92)
    db.session.add(activity93)
    db.session.add(activity94)
    db.session.add(activity95)
    db.session.add(activity96)
    db.session.add(activity97)
    db.session.add(activity98)
    db.session.add(activity99)
    db.session.add(activity100)
    db.session.add(activity101)
    db.session.add(activity102)
    db.session.add(activity103)
    db.session.add(activity104)
    db.session.add(activity105)
    db.session.add(activity106)
    db.session.add(activity107)
    db.session.add(activity108)
    db.session.add(activity109)
    db.session.add(activity110)
    db.session.add(activity111)
    db.session.add(activity112)
    db.session.add(activity113)
    db.session.add(activity114)
    db.session.add(activity115)
    db.session.add(activity116)
    db.session.add(activity117)
    db.session.add(activity118)
    db.session.add(activity119)
    db.session.add(activity120)
    db.session.add(activity121)
    db.session.add(activity122)
    db.session.add(activity123)
    db.session.add(activity124)
    db.session.add(activity125)
    db.session.add(activity126)
    db.session.add(activity127)
    db.session.add(activity128)
    db.session.add(activity129)
    db.session.add(activity130)
    db.session.add(activity131)
    db.session.add(activity132)
    db.session.add(activity133)
    db.session.add(activity134)
    db.session.add(activity135)
    db.session.add(activity136)
    db.session.add(activity137)
    db.session.add(activity138)
    db.session.add(activity139)
    db.session.add(activity140)
    db.session.add(activity141)
    db.session.add(activity142)
    db.session.add(activity143)
    db.session.add(activity144)
    db.session.add(activity145)
    db.session.add(activity146)
    db.session.add(activity147)
    db.session.add(activity148)
    db.session.add(activity149)
    db.session.add(activity150)
    db.session.add(activity151)

    db.session.commit()


def undo_activities():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.activities RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM activities"))

    db.session.commit()
