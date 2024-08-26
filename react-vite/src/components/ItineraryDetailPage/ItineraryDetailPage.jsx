import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate, Link } from "react-router-dom";
import { thunkItineraryById } from "../../redux/itinerary";
import { thunkAddCollection } from "../../redux/collection";
import { thunkAllComments, thunkDeleteComment, thunkNewComment } from "../../redux/comment";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import { FaLocationArrow } from "react-icons/fa6";
import { FaDeleteLeft } from "react-icons/fa6";
import { FaEdit } from "react-icons/fa";
import Map from "../SubComponents/Map"
import Loading from "../SubComponents/Loading";
import "./ItineraryDetailPage.css";

function ItineraryDetail() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { itineraryId } = useParams();
    const itinerary = useSelector((state) => state.itineraries.itineraryById?.[itineraryId]);
    const user = useSelector((state) => state.session.user);
    const commentsObj = useSelector((state) => state.comments.commentsByItinerary?.[itineraryId]);
    const comments = commentsObj? Object.values(commentsObj): [];
    const schedules = itinerary?.schedules;

    const [commentInput, setCommentInput] = useState('');

    useEffect(() => {
        if (itineraryId) {
          dispatch(thunkItineraryById(itineraryId))
          dispatch(thunkAllComments(itineraryId))
        }
    }, [dispatch, itineraryId]);

    if (!itinerary) return <Loading />;

    const handleCollectClick = async (itineraryId) => {
        if (user) {
            await dispatch(thunkAddCollection(itineraryId));
            navigate('/collections/current')
        }
    };

    const handleAddComment = async () => {
        await dispatch(thunkNewComment({review: commentInput, itinerary_id: itineraryId}));
        setCommentInput('');
    }

    const handleRemoveComment = async (commentId) => {
        await dispatch(thunkDeleteComment(commentId, itineraryId))
    }

    return (
    <main className="itinerary-detail-page">
        <div className="itinerary-content">
            <div className="header">
                <img src={itinerary.preview_image_url} alt={itinerary.title} />
                <h1>{itinerary.title}</h1>
            </div>
            <div className="body">
            <div className="inline">
                <Link to={`/itineraries/traveler/${itinerary.traveler.id}`}>
                <div className="user-profile">
                    <img className="profile-image" src={itinerary.traveler.profile_url} alt={itinerary.traveler_id} /><span>{itinerary.traveler.username}</span>
                </div>
                </Link>
                {user? user?.id == itinerary.traveler?.id? (
                    <div className="detail-page-button" onClick={() => navigate(`/itineraries/${itinerary.id}/edit`)}><button>Edit itinerary</button></div>
                ): <div className="detail-page-button" onClick={() => handleCollectClick(itinerary.id)}><button>Add to collection</button></div>: 
                <div className="detail-page-button">
                    <button>
                    <OpenModalMenuItem
                    itemText="Add to collection"
                    modalComponent={<LoginFormModal text={'Before you do that... please'} />}
                    />
                    </button>
                </div>}
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

            <div className="comments">
                <div>
                    {user? 
                    <div className="post-comment">
                        <img className="profile-image" src={user.profile_url} alt={user.id} />
                        <input type="text" 
                                name="comment"
                                value={commentInput}
                                onChange={e => setCommentInput(e.target.value)}
                                placeholder="Ask a question or share your thoughts!" />
                        <div className="detail-page-button post-button"><button onClick={handleAddComment}>Post</button></div>
                    </div>: null}
                </div>

                <div>
                    {comments? comments.map(comment => (
                        <div key={comment.id} className="all-comments">
                            <div>
                                <img className="profile-image" src={comment.user.profile_url} alt={comment.user.id} />
                            </div>
                            <div className="comment-content">
                                <h3>{comment.user.username}</h3>
                                <p>{comment.review}</p>
                                <p className="time">{comment.updated_at.slice(5, 16)}</p>
                                {user? user.id == comment.user.id?
                                <div className="activity-control">
                                    <span><FaEdit /></span>
                                    <span onClick={() => handleRemoveComment(comment.id)}><FaDeleteLeft /></span>
                                </div>: null: null}
                            </div>
                            
                        </div>
                    )): null}
                </div>
            </div>

            <div className="discover-more" onClick={() => navigate("/itineraries")}><button>Continue explore</button></div>

        </div>
        </div>
        <Map itinerary={itinerary}/>
        
    </main> 
    )
}  


export default ItineraryDetail;
