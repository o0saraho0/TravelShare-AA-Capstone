import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { thunkDeleteItinerary, thunkItinerariesByCurrentUser } from "../../redux/itinerary";
import { useModal } from "../../context/Modal";
import ConfirmDeleteModal from "../SubComponents/ConfirmDeleteModal";
import "./ItinerariesManage.css";

function ItinerariesManage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const { setModalContent, closeModal } = useModal();

    const user = useSelector((state) => state.session.user);
    const itinerariesObj = useSelector((state) => state.itineraries.itinerariesByCurrentUser);
    const itineraries = itinerariesObj? Object.values(itinerariesObj): []

    useEffect(() => {
        dispatch(thunkItinerariesByCurrentUser())
    }, [dispatch]);

    if (!itineraries) return null;

    const handleDeleteClick = (itineraryId) => {
        setModalContent(
          <ConfirmDeleteModal
            onDelete={() => handleDeleteConfirm(itineraryId)}
            onClose={closeModal}
          />
        );
    };
    
    const handleDeleteConfirm = async (itineraryId) => {
        await dispatch(thunkDeleteItinerary(itineraryId, user.id));
        dispatch(thunkItinerariesByCurrentUser())
        closeModal();
    };

    return(
    <main>
        <div className="landing-personal">
            <img src="/images/travel_map.jpg" alt="world-map" />
            <div className="landing-personal-container">
                <h1>Hello, {user.first_name}!</h1>
                <div>
                    <h2>Your trips</h2>
                    <button onClick={() => navigate("/itineraries/new")}>+ Plan new trip</button>
                </div>
                <div>
                    <h2>Your collections</h2>
                    <button onClick={() => navigate("/collections/current")}>View your collections</button>
                </div>
            </div>
        </div>
        <div className="landing-explore">
            <h1>Your itineraries</h1>
            <div className="grid-container">
                {itineraries.map(itinerary => (
                    <div key={itinerary.id} id="itinerary-manage-grid-item">
                        <Link to={`/itineraries/${itinerary.id}`}>
                        <div className="image-container"><img src={itinerary.preview_image_url} alt={itinerary.title}/></div>
                        <div><h3>{itinerary.title}</h3></div>                        
                        </Link>

                        <div className="owner-selection">
                            <button onClick={() => navigate(`/itineraries/${itinerary.id}/edit`)}>Edit</button>
                            <button onClick={() => handleDeleteClick(itinerary.id)}>Delete</button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
        
    </main>
    )
}

export default ItinerariesManage;
