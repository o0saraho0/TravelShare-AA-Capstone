import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { thunkAllItineraries } from "../../redux/itinerary";
import Loading from "../SubComponents/Loading";
import "./ItinerariesListPage.css";

function ItinerariesList() {
  const dispatch = useDispatch();
  const itinerariesObj = useSelector(
    (state) => state.itineraries.allItineraries
  );
  const itineraries = itinerariesObj ? Object.values(itinerariesObj) : [];

  useEffect(() => {
    if (!itinerariesObj) {
      dispatch(thunkAllItineraries());
    }
  }, [dispatch, itinerariesObj]);

  if (!itinerariesObj) return <Loading />;

  return (
    <main>
      <div className="landing-explore">
        <h1>Explore</h1>
        <h2>Popular destinations</h2>
        <div className="grid-container">
          {itineraries.map((itinerary) => (
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
              <Link to={`/itineraries/traveler/${itinerary.traveler.id}`}>
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
      </div>
    </main>
  );
}

export default ItinerariesList;
