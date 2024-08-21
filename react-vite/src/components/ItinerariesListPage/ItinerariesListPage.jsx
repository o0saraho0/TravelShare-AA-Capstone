import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { thunkAllItineraries } from "../../redux/itinerary";
import "./ItinerariesListPage.css";

function ItinerariesList() {
    const dispatch = useDispatch();
    const itinerariesObj = useSelector((state) => state.itineraries.allItineraries);
    const itineraries = itinerariesObj? Object.values(itinerariesObj): [];

    useEffect(() => {
        if (!itinerariesObj) {
          dispatch(thunkAllItineraries())
        }
    }, [dispatch, itinerariesObj]);

    return (
    <main>
        <div className="landing-explore">
                <h1>Explore</h1>
                <h2>Popular destinations</h2>
                <div className="grid-container">
                    {itineraries.map((itinerary) => (
                        <div key={itinerary.id} className="grid-item">
                            <Link to={`/itineraries/${itinerary.id}`}>
                            <div className="image-container"><img src={itinerary.preview_image_url} alt={itinerary.title}/></div>
                            <div><h3>{itinerary.title}</h3></div>
                            <div><p>{itinerary.description}</p></div>
                            <div className="user-profile">
                                <img className="profile-image" src={itinerary.traveler.profile_url} alt={itinerary.traveler_id} />{itinerary.traveler.username}
                            </div>
                            </Link>
                        </div>
                    ))}
                </div>
            </div>
    </main>
    )
}

export default ItinerariesList;

