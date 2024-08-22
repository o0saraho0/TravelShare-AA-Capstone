const ConfirmDeleteModal = ({ onDelete, onClose }) => (
    <div className="confirm-deletion">
      <h2>You are about to delete 1 itinerary</h2>
      <p>Keep in mind that deleted itinerary can not be retrieved.</p>
      <button className="delete-yes" onClick={onDelete}>Yes, delete</button>
      <button className="delete-no" onClick={onClose}>No, keep it</button>
    </div>
);

export default ConfirmDeleteModal;