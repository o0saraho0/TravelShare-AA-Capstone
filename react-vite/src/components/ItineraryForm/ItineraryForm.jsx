import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { thunkNewItinerary, thunkEditItinerary } from "../../redux/itinerary";
import { thunkUploadImage, thunkEditImage } from "../../redux/image";
import AIChat from "../AIChat/AIChat";
import "./ItineraryForm.css";

function ItineraryForm({ itinerary, formType }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.session.user);

  const [title, setTitle] = useState("");
  const [countries, setCountries] = useState([]);
  const [selectedCountry, setSelectedCountry] = useState("");
  const [duration, setDuration] = useState(0);
  const [description, setDescription] = useState("");
  const [preview_image_url, setPreviewImage] = useState(null);
  const [previewImageSrc, setPreviewImageSrc] = useState(null);
  const [category_id, setCategoryId] = useState("");
  const [errors, setErrors] = useState({});
  const [imageLoading, setImageLoading] = useState(false);
  const [originalDuration, setOriginalDuration] = useState(null);

  useEffect(() => {
    if (itinerary) {
      setTitle(itinerary.title || "");
      setSelectedCountry(itinerary.country || "");
      setDuration(itinerary.duration || 0);
      setDescription(itinerary.description || "");
      setPreviewImage(itinerary.preview_image_url || null);
      setPreviewImageSrc(itinerary.preview_image_url || null);
      setCategoryId(itinerary.category_id || "");
      setOriginalDuration(itinerary.duration || 0);
    }
  }, [itinerary]);

  useEffect(() => {
    const fetchCountries = async () => {
      try {
        const response = await fetch("https://restcountries.com/v3.1/all");
        const data = await response.json();
        const countryNames = data.map((country) => country.name.common);
        setCountries(countryNames);
      } catch (error) {
        console.error("Error fetching countries:", error);
      }
    };

    fetchCountries();
  }, []);

  const handleCountryChange = (e) => {
    setSelectedCountry(e.target.value);
  };

  const validateForm = () => {
    const errorObj = {};
    const ALLOWED_EXTENSIONS = new Set(["pdf", "png", "jpg", "jpeg", "gif"]);

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
    if (!selectedCountry) errorObj.selectedCountry = "Country is required.";
    if (!category_id) errorObj.category_id = "Category is required.";

    if (formType === "Create New Itinerary" && !preview_image_url) {
      errorObj.preview_image_url = "Preview image is required.";
    } else if (preview_image_url instanceof File) {
      const fileExtension = preview_image_url.name
        .split(".")
        .pop()
        .toLowerCase();
      if (!ALLOWED_EXTENSIONS.has(fileExtension)) {
        errorObj.preview_image_url =
          "Unsupported file type. Please upload a file in one of the following formats: pdf, png, jpg, jpeg, gif.";
      }
    }
    return errorObj;
  };

  const handleImageUpload = async () => {
    if (preview_image_url instanceof File) {
      setImageLoading(true);
      const formData = new FormData();
      formData.append("preview_image_url", preview_image_url);

      let imageResponse;
      if (formType === "Update Your Itinerary") {
        imageResponse = await dispatch(thunkEditImage(formData, itinerary.id));
      } else {
        imageResponse = await dispatch(thunkUploadImage(formData));
      }

      setImageLoading(false);

      if (imageResponse && imageResponse.preview_image_url) {
        return imageResponse.preview_image_url;
      } else {
        setErrors({ preview_image_url: "Failed to upload image." });
        return null;
      }
    }
    return preview_image_url;
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setPreviewImage(file);
    setPreviewImageSrc(URL.createObjectURL(file));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formErrors = validateForm();
    if (Object.values(formErrors).length > 0) {
      setErrors(formErrors);
      return;
    }
    setErrors({});

    const imageUrl = await handleImageUpload();
    if (!imageUrl) return;

    const itineraryData = {
      title,
      country: selectedCountry,
      duration,
      description,
      preview_image_url: imageUrl,
      category_id,
      traveler_id: user.id,
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
      <form
        onSubmit={handleSubmit}
        className="itinerary-form"
        encType="multipart/form-data"
      >
        <h1>{formType}</h1>
        <div>
          <label>
            <h3>Title</h3>
          </label>
          <p>
            Enter a descriptive name that highlights the key destination or
            theme of your trip. A clear title with relevant keywords will
            improve search visibility and help travelers quickly understand the
            trip&apos;s focus.
          </p>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          {errors.title && <p className="error">{errors.title}</p>}
        </div>

        <div>
          <label>
            <h3>Country</h3>
          </label>
          <select value={selectedCountry} onChange={handleCountryChange}>
            <option value="">Select a Country</option>
            {countries.sort().map((country) => (
              <option key={country} value={country}>
                {country}
              </option>
            ))}
          </select>
          {errors.selectedCountry && (
            <p className="error">{errors.selectedCountry}</p>
          )}
        </div>

        <div>
          <div>
            <label>
              <h3>Category</h3>
            </label>
            <p>
              Select the most appropriate category that best describes the style
              of your trip.
            </p>
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
            <p>
              Specify the total number of days for the trip, helping travelers
              understand the commitment.
            </p>
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
            Provide a detailed summary of the main attractions and any unique
            experiences travelers will enjoy. Mention notable sites, activities,
            and any special highlights to attract interest and optimize search
            results.
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
            Add an image that represents your itinerary. This image will be used
            as a preview and cover image of your itinerary.
          </p>
          <div className="image-upload-container">
            <input
              type="file"
              accept="image/*"
              name="preview_image_url"
              onChange={handleImageChange}
            />
            {previewImageSrc && (
              <div className="image-preview">
                <img src={previewImageSrc} alt="preview" />
              </div>
            )}
            {errors.preview_image_url && (
              <p className="error">{errors.preview_image_url}</p>
            )}
          </div>
        </div>

        <div className="landing-signed-in button-center">
          <button type="submit" disabled={imageLoading}>
            {imageLoading ? "Uploading image..." : "Continue to activities"}
          </button>
        </div>
      </form>
      <AIChat />
    </main>
  );
}

export default ItineraryForm;
