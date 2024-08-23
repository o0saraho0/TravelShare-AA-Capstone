const GET_COLLECTIONS = "collections/getFav";
const ADD_COLLECTION = "collections/addFav";
const REMOVE_COLLECTION = "collections/removeFav";

const getFav = (userId, collections) => ({
  type: GET_COLLECTIONS,
  payload: collections,
  userId,
});

const addFav = (collection) => ({
  type: ADD_COLLECTION,
  payload: collection,
});

const removeFav = (collection) => ({
  type: REMOVE_COLLECTION,
  payload: collection,
});

export const thunkAllCollections = (userId) => async (dispatch) => {
  const response = await fetch("/api/collections/current");
  const data = await response.json();
  if (response.ok) {
    dispatch(getFav(userId, data));
    return data;
  }
  return data;
};

export const thunkAddCollection = (itineraryId) => async (dispatch) => {
  const response = await fetch(`/api/collections/${itineraryId}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(itineraryId),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(addFav(data));
    return data;
  }
  return response;
};

export const thunkRemoveCollection = (itineraryId) => async (dispatch) => {
  const response = await fetch(`/api/collections/${itineraryId}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(removeFav(data));
    return data;
  }
  return response;
};

const initialState = {};

function collectionReducer(state = initialState, action) {
  switch (action.type) {
    case GET_COLLECTIONS: {
      const newState = { ...state };
      const collections = {};
      action.payload.forEach((collection) => {
        collections[collection.id] = collection;
      });
      newState[action.userId] = collections;
      return newState;
    }
    case ADD_COLLECTION: {
      const newState = { ...state[action.payload.user_id] };
      newState[action.payload.id] = action.payload;
      return { ...state, [action.payload.user_id]: newState };
    }
    case REMOVE_COLLECTION: {
      const newState = { ...state[action.payload.user_id] };
      delete newState[action.payload.id];
      return { ...state, [action.payload.user_id]: newState };
    }
    default:
      return state;
  }
}

export default collectionReducer;
