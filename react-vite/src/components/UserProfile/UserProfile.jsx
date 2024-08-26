import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from "react-router-dom";
import { thunkAllItineraries } from "../../redux/itinerary";
import Loading from "../SubComponents/Loading";
import "./UserProfile.css";

function UserProfile() {
    const dispatch = useDispatch();
    const {travelerId} = useParams();

    const itinerariesObj = useSelector((state) => state.itineraries.allItineraries);
    const itineraries = itinerariesObj? Object.values(itinerariesObj): [];
    const filteredItineraries = itineraries.filter((el) => el.traveler.id == travelerId)

    useEffect(() => {
        if (!itinerariesObj) {
            dispatch(thunkAllItineraries())
        }
    }, [dispatch, itinerariesObj]);

    if (!itinerariesObj) return <Loading />;

    const itineraryCount = filteredItineraries.length;
    const scheduleCount = filteredItineraries.reduce((total, itinerary) => {
        return total + itinerary.schedules.length;
    }, 0);
    const activityCount = filteredItineraries.reduce((totalActivities, itinerary) => {
        return totalActivities + itinerary.schedules.reduce((total, schedule) => {
            return total + schedule.activities.length;
        }, 0);
    }, 0);

    return(
    <main>
        <div className="traveler-personal">
            <div className="traveler-personal-profile">
                <img className="profile-image" src={filteredItineraries[0].traveler.profile_url} alt={travelerId} />
                <h2>{filteredItineraries[0].traveler.username}</h2>
            </div>
            <div className="landing-personal-container">
                <div className="travel-stats">
                    <div>{filteredItineraries[0].traveler.first_name} has been on <span className="highlight">{itineraryCount}</span> trips</div>
                    <div>has traveled for a total of <span className="highlight">{scheduleCount}</span> days</div>
                    <div>and been to <span className="highlight">{activityCount}</span> places</div>
                </div>
            </div>
        </div>
        <div className="landing-explore">
            <h1>Posted itineraries</h1>
            {filteredItineraries.length?
            <div className="grid-container">
                {filteredItineraries.map(itinerary => (
                    <div key={itinerary.id} className="grid-item">
                    <Link to={`/itineraries/${itinerary.id}`}>
                    <div className="image-container"><img src={itinerary.preview_image_url} alt={itinerary.title}/></div>
                    <div><h3>{itinerary.title}</h3></div>
                    <div className="list-page-duration"><p>Duration: {itinerary.duration} days</p></div>
                    <div className="list-page-description"><p>{itinerary.description}</p></div>
                    </Link>
                </div>
                ))}
            </div>
            : <div>This user has not created any itineraries yet. Please check back later.</div>}
        </div>
        
    </main>
    )
}

export default UserProfile;
