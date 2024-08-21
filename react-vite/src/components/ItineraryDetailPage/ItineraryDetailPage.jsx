import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import "./ItineraryDetailPage.css";

function ItineraryDetail() {
    const dispatch = useDispatch();
    const { itineraryId } = useParams();
    const itinerary = useSelector((state) => state.itineraries.itineraryById?.[itineraryId]);
    const schedules = itinerary?.schedules;
    // console.log(schedules);
    

    useEffect(() => {
        if (itineraryId) {
          dispatch(thunkItineraryById(itineraryId)) 
        }
    }, [dispatch, itineraryId]);

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
                {schedules.map(schedule => (
                    <div key={schedule.id} className="schedule-item">
                        <h2>{schedule.day}</h2>
                        {schedule.activities.map(activity => (
                            <div key={activity.id} className="inline">
                                <div className="activity-info">
                                    <h3>{activity.id} {activity.place}</h3>
                                    <p>{activity.description}</p>
                                </div>
                                <div className="activity-image">
                                    <img src={activity.place_image_url} alt={activity.id} />
                                </div>
                            </div>
                        ))}
                    </div>
                ))}
            </div>     
        </div>
        </div>
        <div className="map">
            
        </div>
    </main> 
    )
}  


export default ItineraryDetail;
