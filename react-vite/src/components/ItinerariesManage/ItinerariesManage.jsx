import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import {
  thunkDeleteItinerary,
  thunkItinerariesByCurrentUser,
} from "../../redux/itinerary";
import { useModal } from "../../context/Modal";
import ConfirmDeleteModal from "../SubComponents/ConfirmDeleteModal";
import Loading from "../SubComponents/Loading";
import AIChat from "../AIChat/AIChat";
import "./ItinerariesManage.css";

function ItinerariesManage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { setModalContent, closeModal } = useModal();

  const user = useSelector((state) => state.session.user);
  const itinerariesObj = useSelector(
    (state) => state.itineraries.itinerariesByCurrentUser
  );
  const itineraries = itinerariesObj ? Object.values(itinerariesObj) : [];

  useEffect(() => {
    if (!itinerariesObj) {
      dispatch(thunkItinerariesByCurrentUser());
    }
  }, [dispatch, itinerariesObj]);

  if (!itinerariesObj) return <Loading />;

  const itineraryCount = itineraries.length;
  const scheduleCount = itineraries.reduce((total, itinerary) => {
    return total + itinerary.schedules.length;
  }, 0);
  const activityCount = itineraries.reduce((totalActivities, itinerary) => {
    return (
      totalActivities +
      itinerary.schedules.reduce((total, schedule) => {
        return total + schedule.activities.length;
      }, 0)
    );
  }, 0);

  const handleDeleteClick = (itineraryId) => {
    setModalContent(
      <ConfirmDeleteModal
        onDelete={() => handleDeleteConfirm(itineraryId)}
        onClose={closeModal}
        message={"Keep in mind that deleted itinerary can not be retrieved."}
      />
    );
  };

  const handleDeleteConfirm = async (itineraryId) => {
    await dispatch(thunkDeleteItinerary(itineraryId));
    closeModal();
  };

  return (
    <main>
      <div className="landing-personal">
        <img src="/images/travel_map.jpg" alt="world-map" />

        <div className="landing-personal-container">
          <h1>Hello, {user.first_name}!</h1>
          <div>
            <div>
              You have been on{" "}
              <span className="highlight">{itineraryCount}</span> trips
            </div>
            <div>
              You have traveled for a total of{" "}
              <span className="highlight">{scheduleCount}</span> days
            </div>
            <div>
              Your journeys have taken you to{" "}
              <span className="highlight">{activityCount}</span> places
            </div>
          </div>
          <div>
            <h2>Your trips</h2>
            <button onClick={() => navigate("/itineraries/new")}>
              + Plan new trip
            </button>
          </div>
          <div>
            <h2>Your collections</h2>
            <button onClick={() => navigate("/collections/current")}>
              View your collections
            </button>
          </div>
        </div>
      </div>
      <div className="landing-explore">
        <h1>Your itineraries</h1>
        {itineraries.length ? (
          <div className="grid-container">
            {itineraries.map((itinerary) => (
              <div
                key={itinerary.id}
                id="itinerary-manage-grid-item"
                className="manage-item"
              >
                <Link to={`/itineraries/${itinerary.id}`}>
                  <div className="image-container">
                    <img
                      src={itinerary.preview_image_url}
                      alt={itinerary.title}
                    />
                  </div>
                </Link>
                <div className="one-line-title">
                  <h3>{itinerary.title}</h3>
                </div>
                <p className="time">{itinerary.updated_at.slice(0, 16)}</p>
                <div className="owner-selection">
                  <button
                    onClick={() =>
                      navigate(`/itineraries/${itinerary.id}/edit`)
                    }
                  >
                    Edit
                  </button>
                  <button onClick={() => handleDeleteClick(itinerary.id)}>
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div>
            You have not created any itineraries yet. Start planning your next
            adventure now!
          </div>
        )}
      </div>
      <AIChat />
    </main>
  );
}

export default ItinerariesManage;
