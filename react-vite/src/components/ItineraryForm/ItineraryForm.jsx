import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkNewItinerary, thunkItinerariesByCurrentUser } from "../../redux/itinerary";
import "./ItineraryForm.css";

function ItineraryForm() {
  const [title, setTitle] = useState("");
  const [duration, setDuration] = useState();
  const [description, setDescription] = useState("");
  const [previewImage, setPreviewImage] = useState("");
  const [categoryId, setCategoryId] = useState();
  const [errors, setErrors] = useState({});

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const user = useSelector((state) => state.session.user);

  const validateForm = () => {
    const errorObj = {};

    if (!title) errorObj.title = "Title is required."
    if (duration <= 0) errorObj.duration = "Duration must be at least 1. Please enter a positive value."
    if (!description) errorObj.description = "Description is required."
    if (description.length < 10) errorObj.description = "Description must be at least 10 characters long. Please provide more details on your itinerary."
    if (!categoryId) errorObj.category = "Category is required."
    if (!previewImage) errorObj.previewImage = "A valid URL is required for the preview image.";
    return errorObj;
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formErrors = validateForm();
    if (Object.values(formErrors).length > 0) {
      setErrors(formErrors);
      return;
    }
    setErrors({});

    const new_itinerary = {
      title,
      duration,
      description,
      previewImage,
      traveler_id: user.id,
      categoryId
    };

    const result = await dispatch(thunkNewItinerary(new_itinerary));
    const itineraryId = result.id;

    if (result.errors) {
      setErrors(result.errors);
    } else {
      navigate(`/products/${itineraryId}`);
    }
  };

  return (
    <main>
        <form onSubmit={handleSubmit} className="itinerary-form">
        <div>
            <label>
            <h3>Title</h3>
            </label>
            <p>Enter the title of your itinerary. This should be a brief, descriptive name that encapsulates the theme or main destination of the trip.</p>
            <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            />
            {errors.title && <p className="error">{errors.title}</p>}
        </div>

        <div className="form-same-line">
            <div>
                <label>
                <h3>Category</h3>
                </label>
                <div className="select-container">
                <select
                    name="categoryId"
                    value={categoryId}
                    onChange={(e) => setCategoryId(e.target.value)}
                >
                    <option value="0">Select a Category</option>
                    <option value="1">City Exploration</option>
                    <option value="2">Nature Escapes</option>
                    <option value="3">Road Trips</option>
                </select>
                </div>
                {errors.categoryId && <p className="error">{errors.categoryId}</p>}
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
            <p>Describe the main attractions, the pace of the trip, and any unique experiences travelers will enjoy.</p>
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
            <p>Add a URL for an image that represents your itinerary. This image will be used as a preview or cover image and should visually capture the essence of the trip.</p>
            <input
            value={previewImage}
            onChange={(e) => setPreviewImage(e.target.value)}
            ></input>
            {errors.previewImage && <p className="error">{errors.previewImage}</p>}
        </div>

        <div className="landing-signed-in button-center">
            <button type="submit">Next</button>
        </div>
        </form>
    </main>
  )
}

export default ItineraryForm;
