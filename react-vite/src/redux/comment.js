const COMMENTS_BY_ITINERARY = "comment/commentByItinerary";
const CREATE_COMMENT = "comment/createComment";
const DELETE_COMMENT = "comment/deleteComment";
const EDIT_COMMENT = "comment/editComment";

const commentByItinerary = (itineraryId) => ({
  type: COMMENTS_BY_ITINERARY,
  payload: itineraryId,
});

const createComment = (comment) => ({
  type: CREATE_COMMENT,
  payload: comment,
});

const deleteComment = (commentId, itineraryId) => ({
  type: DELETE_COMMENT,
  payload: { commentId, itineraryId },
});

const editComment = (comment) => ({
  type: EDIT_COMMENT,
  payload: comment,
});

// get comments by itinerary id
export const thunkAllComments = (itineraryId) => async (dispatch) => {
  const response = await fetch(`/api/comments/itineraries/${itineraryId}`);
  const data = await response.json();
  if (response.ok) {
    dispatch(commentByItinerary(data));
    return data;
  }
  return data;
};

// create comment
export const thunkNewComment = (comment) => async (dispatch) => {
  const response = await fetch(
    `/api/comments/itineraries/${comment.itinerary_id}/new`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(comment),
    }
  );
  const data = await response.json();

  if (response.ok) {
    dispatch(createComment(data));
    return data;
  }
  return data;
};

// delete comment
export const thunkDeleteComment =
  (commentId, itineraryId) => async (dispatch) => {
    const response = await fetch(`/api/comments/${commentId}`, {
      method: "DELETE",
    });
    const data = await response.json();

    if (response.ok) {
      dispatch(deleteComment(commentId, itineraryId));
      return data;
    }
    return data;
  };

// edit comment
export const thunkEditComment = (comment) => async (dispatch) => {
  const response = await fetch(`/api/comments/${comment.id}/edit`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(comment),
  });
  const data = await response.json();

  if (response.ok) {
    dispatch(editComment(data));
    return data;
  }
  return data;
};

const initialState = {};

function commentReducer(state = initialState, action) {
  switch (action.type) {
    case COMMENTS_BY_ITINERARY: {
      let newState = { ...state.commentsByItinerary };
      action.payload.forEach((comment) => {
        const itineraryId = comment.itinerary_id;
        if (!newState[itineraryId]) {
          newState[itineraryId] = {};
        }
        newState[itineraryId][comment.id] = comment;
      });
      return { ...state, commentsByItinerary: newState };
    }
    case CREATE_COMMENT: {
      const itineraryId = action.payload.itinerary_id;
      const newState = { ...state.commentsByItinerary };
      if (!newState[itineraryId]) {
        newState[itineraryId] = {};
      }
      newState[itineraryId][action.payload.id] = action.payload;
      return { ...state, commentsByItinerary: newState };
    }
    case DELETE_COMMENT: {
      const { commentId, itineraryId } = action.payload;
      const newState = { ...state.commentsByItinerary };
      if (newState[itineraryId]) {
        const updatedComments = { ...newState[itineraryId] };
        delete updatedComments[commentId];
        newState[itineraryId] = updatedComments;
      }
      return {
        ...state,
        commentsByItinerary: newState,
      };
    }
    case EDIT_COMMENT: {
      const updatedComment = action.payload;
      const itineraryId = updatedComment.itinerary_id;
      return {
        ...state,
        commentsByItinerary: {
          ...state.commentsByItinerary,
          [itineraryId]: {
            ...state.commentsByItinerary[itineraryId],
            [updatedComment.id]: updatedComment,
          },
        },
      };
    }
    default:
      return state;
  }
}

export default commentReducer;
