import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import { thunkNewActivity, thunkDeleteActivity, thunkUpdateActivity } from "../../redux/activity";
import { FaLocationArrow } from "react-icons/fa6";
import { FaDeleteLeft } from "react-icons/fa6";
import { FaEdit } from "react-icons/fa";
import Loading from "../SubComponents/Loading";
import Map from "../SubComponents/Map"
import "./ActivitiesForm.css";

function ActivitiesForm() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { itineraryId } = useParams();
    const itinerary = useSelector((state) => state.itineraries.itineraryById?.[itineraryId]);
    const schedules = itinerary?.schedules;
    const [showActivityForm, setShowActivityForm] = useState(false);
    const [isEditing, setIsEditing] = useState(false);
    const [currentActivityId, setCurrentActivityId] = useState(null);
    const [errors, setErrors] = useState({});

    const [activityData, setActivityData] = useState({
        place: "",
        longitude: "",
        latitude: "",
        description: "",
        place_image_url: "",
        schedule_id: null,
    });

    useEffect(() => {
        if (itineraryId) {
          dispatch(thunkItineraryById(itineraryId))
        }
    }, [dispatch, itineraryId]);

    const handleAddActivityClick = (scheduleId) => {
        setShowActivityForm(true);
        setActivityData({ ...activityData, schedule_id: scheduleId });
    };

    const handleInputChange = (e) => {
        setActivityData({ ...activityData, [e.target.name]: e.target.value });
    };

    const resetForm = () => {
        setActivityData({
            place: "",
            longitude: "",
            latitude: "",
            description: "",
            place_image_url: "",
            schedule_id: null,
        });
        setShowActivityForm(false);
        setIsEditing(false);
        setCurrentActivityId(null);
        setErrors({});
    };

    const handleEditActivity = (activity) => {
        setActivityData({
            place: activity.place,
            longitude: activity.longitude,
            latitude: activity.latitude,
            description: activity.description,
            place_image_url: activity.place_image_url,
            schedule_id: activity.schedule_id,
        });
        setCurrentActivityId(activity.id);
        setIsEditing(true);
        setShowActivityForm(true);
    };

    const handleRemoveActivity = async (activityId) => {
        console.log(activityId);
        await dispatch(thunkDeleteActivity(activityId));
        await dispatch(thunkItineraryById(itineraryId));
    };

    const validateForm = () => {
        const newErrors = {};
        if (!activityData.place) newErrors.place = "Place is required";
        if (!activityData.longitude || isNaN(activityData.longitude)) newErrors.longitude = "Valid longitude is required";
        if (!activityData.latitude || isNaN(activityData.latitude)) newErrors.latitude = "Valid latitude is required";
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    }

    const handleFormSubmit = async (e) => {
        e.preventDefault();

        if (!validateForm()) {
            return;
        }
    
        if (isEditing && currentActivityId) {
            const updatedActivity = await dispatch(thunkUpdateActivity({...activityData, id: currentActivityId}));
            if (updatedActivity) {
                await dispatch(thunkItineraryById(itineraryId));
                resetForm();
            }
        } else {
            const newActivity = await dispatch(thunkNewActivity(activityData));
            if (newActivity) {
                await dispatch(thunkItineraryById(itineraryId));
                resetForm();
            }
        }
    };

    if (!itinerary) return <Loading />;

    return (
    <main className="itinerary-detail-page activity-edit-page">
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
                <div className="detail-page-button"><button onClick={() => navigate(`/itineraries/${itinerary.id}/edit`)}>
                Edit itinerary</button></div>
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
                                    <div className="activity-control">
                                        <span onClick={() => handleEditActivity(activity)}><p>Edit activity</p><FaEdit /></span>
                                        <span onClick={() => handleRemoveActivity(activity.id)}><p>Remove activity</p><FaDeleteLeft /></span>
                                       
                                        
                                    </div>
                                </div>
                                <div className="activity-image">
                                    {activity.place_image_url && <img src={activity.place_image_url} alt={activity.id} />}
                                    
                                </div>
                            </div>
                        ))}
                    <div onClick={() => handleAddActivityClick(schedule.id)} className="add-day-activity"><button>+ Add activity</button></div>
                    {showActivityForm && activityData.schedule_id === schedule.id && (
                        <form onSubmit={handleFormSubmit} className="activity-form">
                            <input
                                type="text"
                                name="place"
                                value={activityData.place}
                                onChange={handleInputChange}
                                placeholder="Place"
                            />
                            {errors.place && <p className="error">{errors.place}</p>}
                            <input
                                type="text"
                                name="longitude"
                                value={activityData.longitude}
                                onChange={handleInputChange}
                                placeholder="Longitude"
                            />
                            {errors.longitude && <p className="error">{errors.longitude}</p>}
                            <input
                                type="text"
                                name="latitude"
                                value={activityData.latitude}
                                onChange={handleInputChange}
                                placeholder="Latitude"
                            />
                            {errors.latitude && <p className="error">{errors.latitude}</p>}
                            <textarea
                                name="description"
                                value={activityData.description}
                                onChange={handleInputChange}
                                placeholder="Description"
                            />
                            <input
                                type="text"
                                name="place_image_url"
                                value={activityData.place_image_url}
                                onChange={handleInputChange}
                                placeholder="Image URL"
                            />
                            <button type="submit">Save</button>
                        </form>
                    )}
                    </div>
                ))}
            </div>
            </div>
            <div className="confirm-info" onClick={() => navigate(`/itineraries/${itinerary.id}`)}><button>Submit</button></div>
        </div>
        <Map itinerary={itinerary}/>    
    </main> 
    )
}  


export default ActivitiesForm;
