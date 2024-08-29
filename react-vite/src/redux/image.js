const UPLOAD_IMAGE = "image/UPLOAD_IMAGE";
const EDIT_IMAGE = "image/EDIT_IMAGE";

const uploadImage = (image) => ({
  type: UPLOAD_IMAGE,
  payload: image,
});

const editImage = (image) => ({
  type: EDIT_IMAGE,
  payload: image,
});

export const thunkUploadImage = (image) => async (dispatch) => {
  const response = await fetch(`/api/images/itineraries/new`, {
    method: "POST",
    body: image,
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(uploadImage(data));
    return data;
  } else {
    console.log("There was an error uploading your image!");
  }
};

export const thunkEditImage = (image, itineraryId) => async (dispatch) => {
  const response = await fetch(`/api/images/itineraries/${itineraryId}`, {
    method: "PUT",
    body: image,
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(editImage(data));
    return data;
  } else {
    console.log("There was an error updating your image!");
  }
};

export const thunkUploadActivityImage = (image) => async (dispatch) => {
  const response = await fetch(`/api/images/activities/new`, {
    method: "POST",
    body: image,
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(uploadImage(data));
    return data;
  } else {
    console.log("There was an error uploading your image!");
  }
};

export const thunkEditActivityImage =
  (image, activityId) => async (dispatch) => {
    const response = await fetch(`/api/images/activities/${activityId}`, {
      method: "PUT",
      body: image,
    });
    if (response.ok) {
      const data = await response.json();
      dispatch(editImage(data));
      return data;
    } else {
      console.log("There was an error updating your image!");
    }
  };

const initialState = { images: {} };

function imageReducer(state = initialState, action) {
  switch (action.type) {
    case UPLOAD_IMAGE: {
      return {
        ...state,
        images: action.payload,
      };
    }
    case EDIT_IMAGE: {
      return {
        ...state,
        images: action.payload,
      };
    }
    default:
      return state;
  }
}

export default imageReducer;
