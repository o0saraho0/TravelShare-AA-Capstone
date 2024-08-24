import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import { thunkAddCollection } from "../../redux/collection";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import { FaLocationArrow } from "react-icons/fa6";
import Map from "../SubComponents/Map"
import Loading from "../SubComponents/Loading";
import "./ItineraryDetailPage.css";

function ItineraryDetail() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { itineraryId } = useParams();
    const itinerary = useSelector((state) => state.itineraries.itineraryById?.[itineraryId]);
    const user = useSelector((state) => state.session.user);
    const schedules = itinerary?.schedules;

    useEffect(() => {
        if (itineraryId) {
          dispatch(thunkItineraryById(itineraryId)) 
        }
    }, [dispatch, itineraryId]);

    if (!itinerary) return <Loading />;

    const handleCollectClick = async (itineraryId) => {
        if (!user) {
            return (
            <OpenModalMenuItem
                modalComponent={<LoginFormModal text={'Before you do that... please'} />}
            />)
        } else {
            await dispatch(thunkAddCollection(itineraryId));
            navigate('/collections/current')
        }
        
    };

    return (
    <main className="itinerary-detail-page">
        <div className="itinerary-content">
            <div className="header">
                <img src={itinerary.preview_image_url} alt={itinerary.title} />
                <h1>{itinerary.title}</h1>
            </div>
            <div className="body">
            <div className="inline">
                <div className="user-profile">
                    <img className="profile-image" src={itinerary.traveler.profile_url} alt={itinerary.traveler_id} /><span>{itinerary.traveler.username}</span>
                </div>
                {user?.id == itinerary.traveler?.id? (
                    <div className="detail-page-button" onClick={() => navigate(`/itineraries/${itinerary.id}/edit`)}><button>Edit itinerary</button></div>
                ): <div className="detail-page-button" onClick={() => handleCollectClick(itinerary.id)}><button>Add to collection</button></div>}
            </div>
            <div className="time">
                <p>{itinerary.updated_at}</p>
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
                                    {activity.description && <p>{activity.description}</p>}
                                </div>
                                {activity.place_image_url && <div className="activity-image"><img src={activity.place_image_url} alt={activity.id} /></div>}
                            </div>
                        ))}
                    </div>
                ))}
            </div>
            <div className="discover-more" onClick={() => navigate("/itineraries")}><button>Continue explore</button></div>

        </div>
        </div>
        <Map itinerary={itinerary}/>
        
    </main> 
    )
}  


export default ItineraryDetail;
