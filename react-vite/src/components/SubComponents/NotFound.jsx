import { useNavigate } from "react-router-dom";

function NotFoundPage() {
  const navigate = useNavigate();
  return (
    <div className="not-found-container">
      <img
        src="/images/not-found.jpg"
        alt="404 Not Found"
        className="not-found-image"
      />
      <div className="landing-signed-in">
        <button onClick={() => navigate("/itineraries")}>Return Home</button>
      </div>
      
    </div>
  );
}

export default NotFoundPage;
