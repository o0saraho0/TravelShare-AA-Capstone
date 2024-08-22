import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import { FaLocationArrow } from "react-icons/fa6";
import Map from "../SubComponents/Map"
import "./ItineraryDetailPage.css";

function ItineraryDetail() {
    const dispatch = useDispatch();
    const { itineraryId } = useParams();
    const itinerary = useSelector((state) => state.itineraries.itineraryById?.[itineraryId]);
    const user = useSelector((state) => state.session.user);
    const schedules = itinerary?.schedules;

    useEffect(() => {
        if (itineraryId) {
          dispatch(thunkItineraryById(itineraryId)) 
        }
    }, [dispatch, itineraryId]);

    if (!itinerary) return null;

    return (
    <main className="itinerary-detail-page">
        <div className="itinerary-content">
            <div className="header">
                <img src={itinerary.preview_image_url} alt={itinerary.title} />
                <h1>{itinerary.title}</h1>
            </div>
            <div className="body">
            <div className="user-profile">
                <img className="profile-image" src={itinerary.traveler.profile_url} alt={itinerary.traveler_id} /><span>{itinerary.traveler.username}</span>
            </div>
            <div className="description">
                <p>{itinerary.description}</p>
            </div>
            <div className="schedules-container">
                {schedules && schedules.map(schedule => (
                    <div key={schedule.id} className="schedule-item">
                        <h2>{schedule.day}</h2>
                        {schedule.activities && schedule.activities.map(activity => (
                            <div key={activity.id} className="activity-item">
                                <div className="activity-info">
                                    <span className="activity-place"><FaLocationArrow />{activity.place}</span> 
                                    <p>{activity.description}</p>
                                </div>
                                <div className="activity-image">
                                    <img src={activity.place_image_url} alt={activity.id} />
                                </div>
                            </div>
                        ))}
                        {user.id == itinerary.traveler.id && (
                            <div className="detail-page-activity-button"><button>+ Add Activity</button></div>
                        )}
                    </div>
                ))}
            </div>
        </div>
        </div>
        <Map itinerary={itinerary}/>
        
    </main> 
    )
}  


export default ItineraryDetail;
