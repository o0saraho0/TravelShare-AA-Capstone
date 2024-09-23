import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import { thunkAllItineraries } from "../../redux/itinerary";
import Loading from "../SubComponents/Loading";
// import Slider from "react-slick";

import "./LandingPage.css";
// import "slick-carousel/slick/slick.css";
// import "slick-carousel/slick/slick-theme.css";

// const settings = {
//   dots: true,
//   arrows: false,
//   infinite: true,
//   speed: 500,
//   slidesToShow: 3,
//   slidesToScroll: 1,
//   responsive: [
//     {
//       breakpoint: 1024,
//       settings: {
//         slidesToShow: 2,
//       },
//     },
//     {
//       breakpoint: 600,
//       settings: {
//         slidesToShow: 1,
//       },
//     },
//   ],
// };

function LandingPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);
  const itinerariesObj = useSelector(
    (state) => state.itineraries.allItineraries
  );
  const itineraries = itinerariesObj ? Object.values(itinerariesObj) : [];

  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    if (!itinerariesObj) {
      dispatch(thunkAllItineraries());
    }
  }, [dispatch, itinerariesObj]);

  if (!itinerariesObj) return <Loading />;

  const nextSlide = () => {
    if (currentSlide < itineraries.length - 3) {
      setCurrentSlide(currentSlide + 1);
    }
  };

  const prevSlide = () => {
    if (currentSlide > 0) {
      setCurrentSlide(currentSlide - 1);
    }
  };

  return (
    <main>
      {user ? (
        <div className="landing-signed-in">
          <div className="landing-personal">
            <img src="/images/travel.gif" alt="travel" />
            <div className="landing-personal-container">
              <h1>Welcome back, {user.first_name}!</h1>
              <div>
                <h2>Your trips</h2>
                <div>
                  <button onClick={() => navigate("/itineraries/current")}>
                    View your itineraries
                  </button>
                </div>
                <div>
                  <button onClick={() => navigate("/itineraries/new")}>
                    + Plan new trip
                  </button>
                </div>
              </div>
              <div>
                <h2>Your collections</h2>
                <div>
                  <button onClick={() => navigate("/collections/current")}>
                    View your collections
                  </button>
                </div>
                <div>
                  <button onClick={() => navigate("/itineraries")}>
                    + Add new collection
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="landing-explore">
            <h1>Explore</h1>
            <h2>Popular destinations</h2>

            {/* <Slider {...settings}> */}
            <div className="slider">
              {/* Left arrow */}
              <button className="arrow" onClick={prevSlide}>
                ◀
              </button>
              <div className="grid-container">
                {itineraries
                  .slice(currentSlide, currentSlide + 3)
                  .map((itinerary) => (
                    <div key={itinerary.id} className="grid-item">
                      <Link to={`/itineraries/${itinerary.id}`}>
                        <div className="image-container">
                          <img
                            src={itinerary.preview_image_url}
                            alt={itinerary.title}
                          />
                        </div>
                        <div className="one-line-title">
                          <h3>{itinerary.title}</h3>
                        </div>
                        <div className="list-page-duration">
                          <p>Duration: {itinerary.duration} days</p>
                        </div>
                        <div className="list-page-description">
                          <p>{itinerary.description}</p>
                        </div>
                      </Link>
                      <Link
                        to={`/itineraries/traveler/${itinerary.traveler.id}`}
                      >
                        <div className="user-profile">
                          <img
                            className="profile-image"
                            src={itinerary.traveler.profile_url}
                            alt={itinerary.traveler_id}
                          />
                          <span>{itinerary.traveler.username}</span>
                        </div>
                      </Link>
                    </div>
                  ))}
              </div>
              {/* </Slider> */}

              {/* Right arrow */}
              <button className="arrow" onClick={nextSlide}>
                ▶
              </button>
            </div>

            <div className="explore-button">
              <button onClick={() => navigate("/itineraries")}>
                Discover more
              </button>
            </div>
          </div>
          <h1></h1>
        </div>
      ) : (
        <div className="landing-signed-out">
          <h1>Hello World</h1>
          <h2>A Travel Guide to Inspire Your Next Adventure</h2>
          <p>
            Traveling is more than just visiting new places; it&apos;s about
            experiencing the world in a way that enriches your soul and fills
            your life with unforgettable memories.
          </p>
          <p>
            Let this guide inspire your next adventure, whether it&apos;s a solo
            journey of self-discovery, a romantic getaway, or a family trip
            filled with laughter and learning...
          </p>

          <div className="landing-signed-out-buttons">
            <button>
              <OpenModalMenuItem
                itemText="Start planning"
                modalComponent={
                  <LoginFormModal text={"Before you do that... please"} />
                }
              />
            </button>
            <button onClick={() => navigate("/itineraries")}>
              Popular destinations
            </button>
          </div>
        </div>
      )}
    </main>
  );
}

export default LandingPage;
