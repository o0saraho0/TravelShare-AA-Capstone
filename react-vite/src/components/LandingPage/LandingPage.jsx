import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { thunkAllItineraries } from "../../redux/itinerary";
import "./LandingPage.css";

function LandingPage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const user = useSelector((state) => state.session.user);
    const itinerariesObj = useSelector((state) => state.itineraries.allItineraries);
    const itineraries = itinerariesObj? Object.values(itinerariesObj): [];

    useEffect(() => {
        if (!itinerariesObj) {
          dispatch(thunkAllItineraries())
        }
    }, [dispatch, itinerariesObj]);
  
    return (
    <main>
        {user? 
        <div className="landing-signed-in">
            <div className="landing-personal">
                <img src="/images/travel_map.jpg" alt="" />
                <div className="landing-personal-container">
                  <h1>Welcome back, {user.first_name}!</h1>
                    <div>
                        <h2>Your trips</h2>
                        <button>+ Plan new trip</button>
                    </div>
                    <div>
                        <h2>Your collections</h2>
                        <button onClick={() => navigate("/itineraries")}>+ Add new collection</button>
                    </div>
                </div>
            </div>
            <div className="landing-explore">
                <h1>Explore</h1>
                <h2>Popular destinations</h2>
                <div className="grid-container">
                    {itineraries.slice(1, 4).map((itinerary) => (
                        <div key={itinerary.id} className="grid-item">
                            <Link to={`/itineraries/${itinerary.id}`}>
                            <div className="image-container"><img src={itinerary.preview_image_url} alt={itinerary.title}/></div>
                            <div><h3>{itinerary.title}</h3></div>
                            <div><p>{itinerary.description}</p></div>
                            <div className="user-profile">
                                <img className="profile-image" src={itinerary.traveler.profile_url} alt={itinerary.traveler_id} />
                                <div>{itinerary.traveler.username}</div>
                            </div>
                            </Link>
                        </div>
                    ))}
                </div>
                <div className="explore-button">
                    <button onClick={() => navigate("/itineraries")}>Discover more</button>
                </div>
                
            </div>
            <h1></h1>
        </div>: 
        <div className="landing-signed-out">
            <h1>Get inspired and share your travel guide to inspire others</h1>

            <button>Start planning</button>
            <button onClick={() => navigate("/itineraries")}>Popular destinations</button>
        </div>}
    </main>
    )
  }
  
  export default LandingPage;
  