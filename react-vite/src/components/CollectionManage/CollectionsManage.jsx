import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import {
  thunkAllCollections,
  thunkRemoveCollection,
} from "../../redux/collection";
import { useModal } from "../../context/Modal";
import ConfirmDeleteModal from "../SubComponents/ConfirmDeleteModal";
import Loading from "../SubComponents/Loading";
import "./CollectionsManage.css";

function CollectionsManage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { setModalContent, closeModal } = useModal();

  const user = useSelector((state) => state.session.user);
  const collectionsObj = useSelector((state) => state.collections[user?.id]);
  const collections = collectionsObj ? Object.values(collectionsObj) : [];

  useEffect(() => {
    if (!collectionsObj) {
      dispatch(thunkAllCollections(user.id));
    }
  }, [dispatch, collectionsObj, user.id]);

  if (!collectionsObj) return <Loading />;

  const handleDeleteClick = (collectionId) => {
    setModalContent(
      <ConfirmDeleteModal
        onDelete={() => handleDeleteConfirm(collectionId)}
        onClose={closeModal}
        message={
          "Sorry to know you want to delete it. You can always add it back later."
        }
      />
    );
  };

  const handleDeleteConfirm = async (collectionId) => {
    await dispatch(thunkRemoveCollection(collectionId));
    closeModal();
  };

  return (
    <main>
      <div className="landing-personal">
        <img src="/images/travel_map.jpg" alt="world-map" />
        <div className="landing-personal-container">
          <h1>Hello, {user.first_name}!</h1>
          <div>
            <h2>Your trips</h2>
            <div className="collection-buttons">
              <button onClick={() => navigate("/itineraries/current")}>
                View your itineraries
              </button>
              <button onClick={() => navigate("/itineraries/new")}>
                + Plan new trip
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="landing-explore">
        <h1>Your collections</h1>
        {collections.length ? (
          <div className="grid-container">
            {collections.map((collection) => (
              <div
                key={collection.id}
                id="itinerary-manage-grid-item"
                className="manage-item"
              >
                <Link to={`/itineraries/${collection.itinerary.id}`}>
                  <div className="image-container">
                    <img
                      src={collection.itinerary.preview_image_url}
                      alt={collection.itinerary.title}
                    />
                  </div>
                </Link>
                <div className="align-left">
                  <div className="one-line-title">
                    <h3>{collection.itinerary.title}</h3>
                  </div>
                  <div className="list-page-description">
                    <p>{collection.itinerary.description}</p>
                  </div>
                  <div className="user-profile">
                    <img
                      className="profile-image"
                      src={collection.itinerary.traveler.profile_url}
                      alt={collection.itinerary.traveler_id}
                    />
                    <div>
                      <p>{collection.itinerary.traveler.username}</p>
                    </div>
                  </div>
                </div>

                <div className="owner-selection">
                  <button
                    onClick={() => handleDeleteClick(collection.itinerary_id)}
                  >
                    Remove
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div>
            You have not collected any itineraries yet. Explore and collect
            inspiring itineraries from other travelers!
          </div>
        )}
      </div>
    </main>
  );
}

export default CollectionsManage;
