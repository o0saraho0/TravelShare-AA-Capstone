import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate, Link } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import {
  thunkAddCollection,
  thunkAllCollections,
} from "../../redux/collection";
import {
  thunkAllComments,
  thunkDeleteComment,
  thunkNewComment,
} from "../../redux/comment";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import CommentFormModal from "../CommentFormModal";
import { useModal } from "../../context/Modal";
import ConfirmDeleteModal from "../SubComponents/ConfirmDeleteModal";
import { FaLocationArrow } from "react-icons/fa6";
import { FaDeleteLeft } from "react-icons/fa6";
import { FaEdit } from "react-icons/fa";
import { IoIosCloseCircleOutline } from "react-icons/io";
import Map from "../SubComponents/Map";
import Loading from "../SubComponents/Loading";
import "./ItineraryDetailPage.css";

function ItineraryDetail() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { itineraryId } = useParams();
  const itinerary = useSelector(
    (state) => state.itineraries.itineraryById?.[itineraryId]
  );
  const user = useSelector((state) => state.session.user);
  const collectionsObj = useSelector((state) => state.collections[user?.id]);
  const collections = collectionsObj ? Object.values(collectionsObj) : [];

  const commentsObj = useSelector(
    (state) => state.comments.commentsByItinerary?.[itineraryId]
  );
  const comments = commentsObj ? Object.values(commentsObj) : [];

  const schedules = itinerary?.schedules;

  const { setModalContent, closeModal } = useModal();
  const [commentInput, setCommentInput] = useState("");
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (itineraryId) {
      dispatch(thunkItineraryById(itineraryId));
      dispatch(thunkAllComments(itineraryId));
    }
    if (user) {
      dispatch(thunkAllCollections(user.id));
    }
  }, [dispatch, itineraryId, user]);

  const isItineraryInCollection = collections?.some(
    (collection) => collection.itinerary_id === parseInt(itineraryId)
  );

  const handleCollectClick = async (itineraryId) => {
    if (user) {
      dispatch(thunkAddCollection(itineraryId)).then(() => {
        const popUpCollected = document.getElementById("collected");
        popUpCollected.style.display = "block";
        setTimeout(() => {
          popUpCollected.style.display = "none";
        }, 3000);
      });
    }
  };

  const handleAddComment = async () => {
    setErrors({});
    if (commentInput.length < 10) {
      setErrors({
        comment: "Please write at least 10 characters to share your thoughts.",
      });
      return;
    }
    await dispatch(
      thunkNewComment({ review: commentInput, itinerary_id: itineraryId })
    );
    setCommentInput("");
  };

  const handleRemoveComment = async (commentId) => {
    setModalContent(
      <ConfirmDeleteModal
        onDelete={() => handleRemoveConfirm(commentId)}
        onClose={closeModal}
        message={"Keep in mind that deleted comment can not be retrieved."}
      />
    );
  };

  const handleRemoveConfirm = async (commentId) => {
    await dispatch(thunkDeleteComment(commentId, itineraryId));
    closeModal();
  };

  const handleDisplayImage = (imageUrl) => {
    setModalContent(
      <div className="image-display">
        <img src={imageUrl} alt="activity-image" />
        <div onClick={() => closeModal()} className="close-display">
          <IoIosCloseCircleOutline />
        </div>
      </div>
    );
  };

  if (!itinerary) return <Loading />;

  return (
    <main className="itinerary-detail-page">
      <div className="itinerary-content">
        <div className="header">
          <img
            src={itinerary.preview_image_url}
            alt={itinerary.title}
            onClick={() => handleDisplayImage(itinerary.preview_image_url)}
          />
          <h1>{itinerary.title}</h1>
        </div>
        <div className="body">
          <div className="inline">
            <Link to={`/itineraries/traveler/${itinerary.traveler.id}`}>
              <div className="user-profile">
                <img
                  className="profile-image"
                  src={itinerary.traveler.profile_url}
                  alt={itinerary.traveler_id}
                />
                <span>{itinerary.traveler.username}</span>
              </div>
            </Link>
            {user ? (
              user?.id == itinerary.traveler?.id ? (
                <div
                  className="detail-page-button"
                  onClick={() => navigate(`/itineraries/${itinerary.id}/edit`)}
                >
                  <button>Edit itinerary</button>
                </div>
              ) : !isItineraryInCollection ? (
                <div
                  className="detail-page-button"
                  onClick={() => handleCollectClick(itinerary.id)}
                >
                  <button>Add to collection</button>
                </div>
              ) : null
            ) : (
              <div className="detail-page-button">
                <button>
                  <OpenModalMenuItem
                    itemText="Add to collection"
                    modalComponent={
                      <LoginFormModal text={"Before you do that... please"} />
                    }
                  />
                </button>
              </div>
            )}
          </div>
          <div className="time">
            <p>{itinerary.updated_at}</p>
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
                          {activity.description && (
                            <div className="activity-description">
                              <p>{activity.description}</p>
                            </div>
                          )}
                        </div>
                        {activity.place_image_url && (
                          <div className="activity-image">
                            <img
                              src={activity.place_image_url}
                              alt={activity.id}
                              onClick={() =>
                                handleDisplayImage(activity.place_image_url)
                              }
                            />
                          </div>
                        )}
                      </div>
                    ))}
                </div>
              ))}
          </div>

          <div className="comments">
            <div>
              {user ? (
                <div>
                  <div className="inline">
                    <div className="post-comment inline">
                      <img
                        className="profile-image"
                        src={user.profile_url}
                        alt={user.id}
                      />
                      <input
                        type="text"
                        name="comment"
                        value={commentInput}
                        onChange={(e) => setCommentInput(e.target.value)}
                        placeholder="Ask a question or share your thoughts!"
                      />
                    </div>
                    <div className="detail-page-button post-button">
                      <button onClick={handleAddComment}>Post</button>
                    </div>
                  </div>
                  <div>
                    {errors.comment && (
                      <p
                        className="error"
                        style={{ marginLeft: "55px", marginTop: "6px" }}
                      >
                        {errors.comment}
                      </p>
                    )}
                  </div>
                </div>
              ) : null}
            </div>

            <div>
              {comments
                ? comments
                    .sort((a, b) => b.id - a.id)
                    .map((comment) => (
                      <div key={comment.id} className="all-comments">
                        <div>
                          <img
                            className="profile-image"
                            src={comment.user.profile_url}
                            alt={comment.user.id}
                          />
                        </div>
                        <div className="comment-content">
                          <h3>{comment.user.username}</h3>
                          <p>{comment.review}</p>
                          <p className="time">
                            {comment.updated_at.slice(5, 16)}
                          </p>
                          {user ? (
                            user.id == comment.user.id ? (
                              <div className="activity-control">
                                <span>
                                  <OpenModalMenuItem
                                    itemText={<FaEdit />}
                                    modalComponent={
                                      <CommentFormModal
                                        itineraryId={itineraryId}
                                        commentId={comment.id}
                                      />
                                    }
                                  />
                                </span>
                                <span
                                  onClick={() =>
                                    handleRemoveComment(comment.id)
                                  }
                                >
                                  <FaDeleteLeft />
                                </span>
                              </div>
                            ) : null
                          ) : null}
                        </div>
                      </div>
                    ))
                : null}
            </div>
          </div>

          <div
            className="discover-more"
            onClick={() => navigate("/itineraries")}
          >
            <button id="greener-button">Continue explore</button>
          </div>
        </div>
      </div>
      <div className="map-container">
        <Map itinerary={itinerary} />
      </div>
    </main>
  );
}

export default ItineraryDetail;
