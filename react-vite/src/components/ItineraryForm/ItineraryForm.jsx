import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkNewItinerary, thunkEditItinerary } from "../../redux/itinerary";
import "./ItineraryForm.css";

function ItineraryForm({ itinerary, formType }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);

  const [title, setTitle] = useState("");
  const [duration, setDuration] = useState(0);
  const [description, setDescription] = useState("");
  const [preview_image_url, setPreviewImage] = useState("");
  const [category_id, setCategoryId] = useState("");
  const [errors, setErrors] = useState({});
  const [originalDuration, setOriginalDuration] = useState(null);

  useEffect(() => {
    if (itinerary) {
      setTitle(itinerary.title || "");
      setDuration(itinerary.duration || 0);
      setDescription(itinerary.description || "");
      setPreviewImage(itinerary.preview_image_url || "");
      setCategoryId(itinerary.category_id || "");
      setOriginalDuration(itinerary.duration || 0);
    }
  }, [itinerary]);

  const validateForm = () => {
    const errorObj = {};

    if (!title) errorObj.title = "Title is required.";
    if (title.length < 5 || title.length > 100)
      errorObj.title =
        "Please enter a title that is between 5 and 100 characters.";
    if (duration <= 0)
      errorObj.duration =
        "Duration must be at least 1. Please enter a positive value.";
    if (!description) errorObj.description = "Description is required.";
    if (description.length < 10)
      errorObj.description =
        "Description must be at least 10 characters long. Please provide more details on your itinerary.";
    if (!category_id) errorObj.category_id = "Category is required.";
    if (formType === "Create New Itinerary" && !preview_image_url)
      errorObj.preview_image_url = "An URL is required for the preview image.";
    return errorObj;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formErrors = validateForm();
    if (Object.values(formErrors).length > 0) {
      setErrors(formErrors);
      return;
    }
    setErrors({});

    const itineraryData = {
      title,
      duration,
      description,
      preview_image_url,
      traveler_id: user.id,
      category_id,
    };

    let newItinerary;
    if (formType === "Update Your Itinerary") {
      itineraryData.originalDuration = originalDuration;
      newItinerary = await dispatch(
        thunkEditItinerary(itineraryData, itinerary.id)
      );
    } else if (formType === "Create New Itinerary") {
      newItinerary = await dispatch(thunkNewItinerary(itineraryData));
    }

    if (newItinerary.errors) {
      setErrors(newItinerary.errors);
    } else {
      navigate(`/itineraries/${newItinerary.id}/activities`);
    }
  };

  return (
    <main>
      <form onSubmit={handleSubmit} className="itinerary-form">
        <h1>{formType}</h1>
        <div>
          <label>
            <h3>Title</h3>
          </label>
          <p>
            Enter the title of your itinerary. This should be a brief,
            descriptive name that encapsulates the theme or main destination of
            the trip.
          </p>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          {errors.title && <p className="error">{errors.title}</p>}
        </div>

        <div>
          <div>
            <label>
              <h3>Category</h3>
            </label>
            <div className="select-container">
              <select
                name="category_id"
                value={category_id}
                onChange={(e) => setCategoryId(e.target.value)}
              >
                <option value="0">Select a Category</option>
                <option value="1">City Exploration</option>
                <option value="2">Nature Escapes</option>
                <option value="3">Road Trips</option>
              </select>
            </div>
            {errors.category_id && (
              <p className="error">{errors.category_id}</p>
            )}
          </div>
          <div>
            <label>
              <h3>Duration</h3>
            </label>
            <input
              type="number"
              min="1"
              step="1"
              value={duration}
              onChange={(e) => setDuration(e.target.value)}
            />
            {errors.duration && <p className="error">{errors.duration}</p>}
          </div>
        </div>

        <div>
          <label>
            <h3>Description</h3>
          </label>
          <p>
            Describe the main attractions, the pace of the trip, and any unique
            experiences travelers will enjoy.
          </p>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
          {errors.description && <p className="error">{errors.description}</p>}
        </div>

        <div>
          <label>
            <h3>Preview Image</h3>
          </label>
          <p>
            Add a URL for an image that represents your itinerary. This image
            will be used as a preview or cover image and should visually capture
            the essence of the trip.
          </p>
          <input
            name={preview_image_url}
            value={preview_image_url}
            onChange={(e) => setPreviewImage(e.target.value)}
          ></input>
          {errors.preview_image_url && (
            <p className="error">{errors.preview_image_url}</p>
          )}
        </div>

        <div className="landing-signed-in button-center">
          <button type="submit">Next</button>
        </div>
      </form>
    </main>
  );
}

export default ItineraryForm;
