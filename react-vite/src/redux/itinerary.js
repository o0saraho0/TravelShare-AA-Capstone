const ALL_ITINERARIES = "itinerary/allItineraries";
const ITINERARY_BY_ID = "itinerary/itineraryById";
const ITINERARIES_BY_CURRENT_USER = "itinerary/itinerariesByCurrentUser";

const allItineraries = (itineraries) => ({
  type: ALL_ITINERARIES,
  payload: itineraries,
});

const itineraryById = (itinerary) => ({
  type: ITINERARY_BY_ID,
  payload: itinerary,
});

const itinerariesByCurrentUser = (itineraries, user_id) => ({
  type: ITINERARIES_BY_CURRENT_USER,
  payload: itineraries,
  user_id,
});

// get itineraries owned by current user
export const thunkItinerariesByCurrentUser = () => async (dispatch) => {
  const response = await fetch("/api/itineraries/current");
  const data = await response.json();
  if (response.ok) {
    dispatch(itinerariesByCurrentUser(data));
    return data;
  }
  return data;
};

// get itinerary by Id
export const thunkItineraryById = (itineraryId) => async (dispatch) => {
  const response = await fetch(`/api/itineraries/${itineraryId}`);
  const data = await response.json();
  if (response.ok) {
    dispatch(itineraryById(data));
    return data;
  }
  return data;
};

// get all itineraries
export const thunkAllItineraries = () => async (dispatch) => {
  const response = await fetch("/api/itineraries");
  const data = await response.json();
  if (response.ok) {
    dispatch(allItineraries(data));
    return data;
  }
  return data;
};

const initialState = {
  itineraryById: {},
};

function itineraryReducer(state = initialState, action) {
  switch (action.type) {
    case ALL_ITINERARIES: {
      let newState = {};
      action.payload.forEach((itinerary) => {
        newState[itinerary.id] = itinerary;
      });
      return { ...state, allItineraries: newState };
    }
    case ITINERARY_BY_ID: {
      let newState = { ...state.itineraryById };
      newState[action.payload.id] = action.payload;
      return { ...state, itineraryById: newState };
    }
    case ITINERARIES_BY_CURRENT_USER: {
      let newState = {};
      action.payload.forEach((itinerary) => {
        newState[itinerary.id] = itinerary;
      });
      return {
        ...state,
        itinerariesByUser: newState,
      };
    }
    default:
      return state;
  }
}

export default itineraryReducer;
