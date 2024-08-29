import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import {
  thunkNewActivity,
  thunkDeleteActivity,
  thunkUpdateActivity,
} from "../../redux/activity";
import {
  thunkUploadActivityImage,
  thunkEditActivityImage,
} from "../../redux/image";
import { FaLocationArrow } from "react-icons/fa6";
import { FaDeleteLeft } from "react-icons/fa6";
import { FaEdit } from "react-icons/fa";
import { useModal } from "../../context/Modal";
import ConfirmDeleteModal from "../SubComponents/ConfirmDeleteModal";
import Loading from "../SubComponents/Loading";
import Map from "../SubComponents/Map";
import "./ActivitiesForm.css";

function ActivitiesForm() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { itineraryId } = useParams();
  const itinerary = useSelector(
    (state) => state.itineraries.itineraryById?.[itineraryId]
  );
  const schedules = itinerary?.schedules;

  const { setModalContent, closeModal } = useModal();
  const [showActivityForm, setShowActivityForm] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentActivityId, setCurrentActivityId] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const [activityData, setActivityData] = useState({
    place: "",
    longitude: "",
    latitude: "",
    description: "",
    place_image_url: null,
    schedule_id: null,
  });

  useEffect(() => {
    if (itineraryId) {
      dispatch(thunkItineraryById(itineraryId));
    }
  }, [dispatch, itineraryId]);

  const handleAddActivityClick = (scheduleId) => {
    setShowActivityForm(true);
    setActivityData({ ...activityData, schedule_id: scheduleId });
  };

  const handleInputChange = (e) => {
    const { name, value, files } = e.target;
    if (name === "place_image_url" && files.length > 0) {
      setActivityData({ ...activityData, [name]: files[0] });
    } else {
      setActivityData({ ...activityData, [name]: value });
    }
  };

  const handleImageUpload = async () => {
    if (activityData.place_image_url instanceof File) {
      setImageLoading(true);
      const formData = new FormData();
      formData.append("place_image_url", activityData.place_image_url);

      let imageResponse;
      if (isEditing && currentActivityId) {
        imageResponse = await dispatch(
          thunkEditActivityImage(formData, currentActivityId)
        );
      } else {
        imageResponse = await dispatch(thunkUploadActivityImage(formData));
      }

      setImageLoading(false);

      if (imageResponse && imageResponse.place_image_url) {
        return imageResponse.place_image_url;
      } else {
        setErrors({ place_image_url: "Failed to upload image." });
        return null;
      }
    }
    return null;
  };

  const updateActivity = (searchPosition) => {
    setActivityData({
      ...activityData,
      longitude: searchPosition.longitude,
      latitude: searchPosition.latitude,
      place: searchPosition.label.split(",")[0],
    });
  };

  const resetForm = () => {
    setActivityData({
      place: "",
      longitude: "",
      latitude: "",
      description: "",
      place_image_url: null,
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
    setModalContent(
      <ConfirmDeleteModal
        onDelete={() => handleRemoveConfirm(activityId)}
        onClose={closeModal}
        message={"Keep in mind that deleted activity can not be retrieved."}
      />
    );
  };

  const handleRemoveConfirm = async (activityId) => {
    await dispatch(thunkDeleteActivity(activityId));
    await dispatch(thunkItineraryById(itineraryId));
    closeModal();
  };

  const validateForm = () => {
    const newErrors = {};
    const ALLOWED_EXTENSIONS = new Set(["pdf", "png", "jpg", "jpeg", "gif"]);
    if (!activityData.place) newErrors.place = "Place is required";
    if (activityData.place.length < 5 || activityData.place.length > 100)
      newErrors.place =
        "Please enter a place name that is between 5 and 100 characters.";
    if (!activityData.longitude || isNaN(activityData.longitude))
      newErrors.longitude = "Valid longitude is required";
    if (!activityData.latitude || isNaN(activityData.latitude))
      newErrors.latitude = "Valid latitude is required";
    if (activityData.place_image_url instanceof File) {
      const fileExtension = activityData.place_image_url.name
        .split(".")
        .pop()
        .toLowerCase();
      if (!ALLOWED_EXTENSIONS.has(fileExtension)) {
        newErrors.place_image_url =
          "Only pdf, png, jpg, jpeg, gif are supported.";
      }
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    const imageUrl = await handleImageUpload();

    const updatedActivityData = {
      ...activityData,
      place_image_url: imageUrl || activityData.place_image_url,
    };

    if (isEditing && currentActivityId) {
      const updatedActivity = await dispatch(
        thunkUpdateActivity({ ...updatedActivityData, id: currentActivityId })
      );
      if (updatedActivity) {
        await dispatch(thunkItineraryById(itineraryId));
        resetForm();
      }
    } else {
      const newActivity = await dispatch(thunkNewActivity(updatedActivityData));
      if (newActivity) {
        await dispatch(thunkItineraryById(itineraryId));
        resetForm();
      }
    }
  };

  const handleCancelClick = () => {
    resetForm();
  };

  if (!itinerary) return <Loading />;

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
              <img
                className="profile-image"
                src={itinerary.traveler.profile_url}
                alt={itinerary.traveler_id}
              />
              <span>{itinerary.traveler.username}</span>
            </div>
            <div className="detail-page-button">
              <button
                onClick={() => navigate(`/itineraries/${itinerary.id}/edit`)}
              >
                Edit itinerary
              </button>
            </div>
          </div>
          <div className="description">
            <p>{itinerary.description}</p>
          </div>
          <div className="schedules-container">
            {schedules &&
              schedules.map((schedule) => (
                <div key={schedule.id} className="schedule-item">
                  <h2>{schedule.day}</h2>
                  {schedule.activities &&
                    schedule.activities.map((activity) => (
                      <div key={activity.id} className="activity-item">
                        <div className="activity-info">
                          <span className="activity-place">
                            <FaLocationArrow />
                            {activity.place}
                          </span>
                          <p>{activity.description}</p>
                          <div className="activity-control">
                            <span onClick={() => handleEditActivity(activity)}>
                              <p>Edit activity</p>
                              <FaEdit />
                            </span>
                            <span
                              onClick={() => handleRemoveActivity(activity.id)}
                            >
                              <p>Remove activity</p>
                              <FaDeleteLeft />
                            </span>
                          </div>
                        </div>
                        <div className="activity-image">
                          {activity.place_image_url && (
                            <img
                              src={activity.place_image_url}
                              alt={activity.id}
                            />
                          )}
                        </div>
                      </div>
                    ))}
                  <div
                    onClick={() => handleAddActivityClick(schedule.id)}
                    className="add-day-activity"
                  >
                    <button>+ Add activity</button>
                  </div>
                  {showActivityForm &&
                    activityData.schedule_id === schedule.id && (
                      <form
                        onSubmit={handleFormSubmit}
                        className="activity-form"
                        encType="multipart/form-data"
                      >
                        <div>
                          <p className="hint">
                            You can use the map search box to find a location
                            <br />
                            and confirm to add to your activity
                            <br />
                          </p>
                        </div>
                        <input
                          type="text"
                          name="place"
                          value={activityData.place}
                          onChange={handleInputChange}
                          placeholder="Place"
                        />
                        {errors.place && (
                          <p className="error">{errors.place}</p>
                        )}
                        <input
                          type="text"
                          name="longitude"
                          value={activityData.longitude}
                          onChange={handleInputChange}
                          placeholder="Longitude"
                        />
                        {errors.longitude && (
                          <p className="error">{errors.longitude}</p>
                        )}
                        <input
                          type="text"
                          name="latitude"
                          value={activityData.latitude}
                          onChange={handleInputChange}
                          placeholder="Latitude"
                        />
                        {errors.latitude && (
                          <p className="error">{errors.latitude}</p>
                        )}
                        <p className="hint">
                          <br />
                          description and image are optional
                        </p>
                        <textarea
                          name="description"
                          value={activityData.description}
                          onChange={handleInputChange}
                          placeholder="Description"
                        />
                        <input
                          type="file"
                          accept="image/*"
                          name="place_image_url"
                          onChange={handleInputChange}
                        />
                        {errors.place_image_url && (
                          <p className="error">{errors.place_image_url}</p>
                        )}

                        <div className="activity-form-buttons">
                          <button type="submit">
                            {imageLoading ? "Uploading" : "Save"}
                          </button>
                          <button type="button" onClick={handleCancelClick}>
                            Cancel
                          </button>
                        </div>
                      </form>
                    )}
                </div>
              ))}
          </div>
        </div>
        <div
          className="confirm-info"
          onClick={() => navigate(`/itineraries/${itinerary.id}`)}
        >
          <button>Submit</button>
        </div>
      </div>
      <Map
        itinerary={itinerary}
        showSearchField={showActivityForm}
        updateAcitivity={updateActivity}
      />
    </main>
  );
}

export default ActivitiesForm;
