import { useModal } from "../../context/Modal";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { thunkEditComment } from "../../redux/comment";
import "./CommentFormModal.css";

function CommentFormModal({ itineraryId, commentId }) {
  const dispatch = useDispatch();
  const [review, setReview] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const preComment = useSelector(
    (state) => state.comments.commentsByItinerary?.[itineraryId]?.[commentId]
  );

  useEffect(() => {
    if (preComment) {
      setReview(preComment.review);
    }
  }, [preComment]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});

    if (review.length < 10) {
      setErrors({
        review: "Please write at least 10 characters to share your thoughts.",
      });
      return;
    }

    const updatedComment = {
      id: commentId,
      review,
      itinerary_id: itineraryId,
      user_id: preComment.user_id,
    };

    await dispatch(thunkEditComment(updatedComment));
    closeModal();
  };

  return (
    <div className="comment-modal">
      <h2>Edit your comment</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Update your review here..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
        {errors.review && <p className="error">{errors.review}</p>}
        <button type="submit">Update</button>
      </form>
    </div>
  );
}

export default CommentFormModal;
