import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate, useParams } from "react-router-dom";
import { thunkAllItineraries } from "../../redux/itinerary";
import Loading from "../SubComponents/Loading";
import "./ItinerariesByCategory.css";

function ItinerariesByCategory() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const {categoryId} = useParams();
    const itinerariesObj = useSelector((state) => state.itineraries.allItineraries);
    const itineraries = itinerariesObj? Object.values(itinerariesObj): [];
    const filteredItineraries = itineraries.filter(itinerary => {
        return itinerary.category_id === Number(categoryId)
    })

    useEffect(() => {
        if (!itinerariesObj) {
          dispatch(thunkAllItineraries())
        }
    }, [dispatch, itinerariesObj]);

    if (!itinerariesObj) return <Loading />;

    if (filteredItineraries.length === 0) return (<div className="text-in-empty-screen">
        <div>Currently, there are no itineraries available for this category.</div>
        <div>Please come back later to discover new adventures!</div>
        <button onClick={() => navigate("/itineraries")}>Discover more</button>
        </div>)

    return (
    <main>
        <div className="landing-explore">
                <h1>Explore</h1>
                <h2>Popular destinations</h2>
                <div className="grid-container">
                    {filteredItineraries.map((itinerary) => (
                        <div key={itinerary.id} className="grid-item">
                            <Link to={`/itineraries/${itinerary.id}`}>
                            <div className="image-container"><img src={itinerary.preview_image_url} alt={itinerary.title}/></div>
                            <div><h3>{itinerary.title}</h3></div>
                            <div className="list-page-duration"><p>Duration: {itinerary.duration} days</p></div>
                            <div className="list-page-description"><p>{itinerary.description}</p></div>
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

export default ItinerariesByCategory;