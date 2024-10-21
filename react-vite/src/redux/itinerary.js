const ALL_ITINERARIES = "itinerary/allItineraries";
const ITINERARY_BY_ID = "itinerary/itineraryById";
const ITINERARIES_BY_CURRENT_USER = "itinerary/itinerariesByCurrentUser";
const CREATE_ITINERARY = "itinerary/createItinerary";
const DELETE_ITINERARY = "itinerary/deleteItinerary";
const EDIT_ITINERARY = "itinerary/editItinerary";
const CLEAR_ITINERARIES = "itinerary/clearItineraries";

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

const createItinerary = (itinerary) => ({
  type: CREATE_ITINERARY,
  payload: itinerary,
});

const deleteItinerary = (itineraryId) => ({
  type: DELETE_ITINERARY,
  payload: itineraryId,
});

const editItinerary = (itinerary) => ({
  type: EDIT_ITINERARY,
  payload: itinerary,
});

export const clearItineraries = () => ({
  type: CLEAR_ITINERARIES,
  payload: {},
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

    const countriesSet = new Set(data.map((itinerary) => itinerary.country));
    const countries = Array.from(countriesSet);
    dispatch({ type: "SET_COUNTRIES", payload: countries });

    return data;
  }
  return data;
};

// create itinerary
export const thunkNewItinerary = (itinerary) => async (dispatch) => {
  const response = await fetch("/api/itineraries/new", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(itinerary),
  });
  const data = await response.json();

  if (response.ok) {
    dispatch(createItinerary(data));
    return data;
  }
  return data;
};

// delete itinerary
export const thunkDeleteItinerary = (itineraryId) => async (dispatch) => {
  const response = await fetch(`/api/itineraries/${itineraryId}`, {
    method: "DELETE",
  });
  const data = await response.json();

  if (response.ok) {
    dispatch(deleteItinerary(itineraryId));
    return data;
  }
  return data;
};

// edit itinerary
export const thunkEditItinerary =
  (itinerary, itineraryId) => async (dispatch) => {
    const response = await fetch(`/api/itineraries/${itineraryId}/edit`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(itinerary),
    });
    const data = await response.json();

    if (response.ok) {
      dispatch(editItinerary(data));
      return data;
    }
    return data;
  };

const initialState = {
  itineraryById: {},
  countries: [],
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
    case "SET_COUNTRIES": {
      return { ...state, countries: action.payload };
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
        itinerariesByCurrentUser: newState,
      };
    }
    case CREATE_ITINERARY: {
      const itineraryId = action.payload.id;
      const newState = {};
      if (state.allItineraries) {
        const newAllItineraries = {
          ...state.allItineraries,
          [itineraryId]: action.payload,
        };
        newState["allItineraries"] = newAllItineraries;
      }

      if (state.itineraryById[itineraryId]) {
        const newItineraryById = {
          ...state.itineraryById,
          [itineraryId]: action.payload,
        };
        newState["itineraryById"] = newItineraryById;
      }

      if (state.itinerariesByCurrentUser) {
        const newItinerariesByCurrentUser = {
          ...state.itinerariesByCurrentUser,
          [itineraryId]: action.payload,
        };
        newState["itinerariesByCurrentUser"] = newItinerariesByCurrentUser;
      }
      return { ...state, ...newState };
    }
    case DELETE_ITINERARY: {
      const itineraryId = action.payload;
      const newState = {};
      if (state.allItineraries) {
        const newAllItineraries = {
          ...state.allItineraries,
        };
        delete newAllItineraries[itineraryId];
        newState["allItineraries"] = newAllItineraries;
      }

      if (state.itineraryById[itineraryId]) {
        const newItineraryById = {
          ...state.itineraryById,
        };
        delete newItineraryById[itineraryId];
        newState["itineraryById"] = newItineraryById;
      }

      if (state.itinerariesByCurrentUser) {
        const newItinerariesByCurrentUser = {
          ...state.itinerariesByCurrentUser,
        };
        delete newItinerariesByCurrentUser[itineraryId];
        newState["itinerariesByCurrentUser"] = newItinerariesByCurrentUser;
      }
      return { ...state, ...newState };
    }
    case EDIT_ITINERARY: {
      const itineraryId = action.payload.id;
      const newState = {};
      if (state.allItineraries) {
        const newAllItineraries = {
          ...state.allItineraries,
          [itineraryId]: {
            ...state.allItineraries[itineraryId],
            ...action.payload,
          },
        };
        newState["allItineraries"] = newAllItineraries;
      }

      if (state.itineraryById[itineraryId]) {
        const newItineraryById = {
          ...state.itineraryById,
          [itineraryId]: {
            ...state.itineraryById[itineraryId],
            ...action.payload,
          },
        };
        newState["itineraryById"] = newItineraryById;
      }

      if (state.itinerariesByCurrentUser) {
        const newItinerariesByCurrentUser = {
          ...state.itinerariesByCurrentUser,
          [itineraryId]: {
            ...state.itinerariesByCurrentUser[itineraryId],
            ...action.payload,
          },
        };
        newState["itinerariesByCurrentUser"] = newItinerariesByCurrentUser;
      }
      return { ...state, ...newState };
    }
    case CLEAR_ITINERARIES: {
      const newState = { ...state };
      delete newState.itinerariesByCurrentUser;
      return newState;
    }
    default:
      return state;
  }
}

export default itineraryReducer;
