import "./SubComponents.css"

const ConfirmDeleteModal = ({ onDelete, onClose, message }) => (
    <div className="confirm-deletion">
      <h2>You are about to delete 1 itinerary</h2>
      <p>{message}</p>
      <div className="inline" style={{gap: "5%"}}>
      <button  onClick={onDelete}>Yes, delete</button>
      <button onClick={onClose}>No, keep it</button>
      </div>
    </div>
);

export default ConfirmDeleteModal;