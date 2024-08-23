const ACTIVITIES_BY_SCHEDULE = "activity/activitiesBySchedule";
const ADD_ACTIVITY = "activity/addActivity";
const DELETE_ACTIVITY = "activity/deleteActivity";
// const EDIT_ACTIVITY = "activity/editActivity";

const activitiesBySchedule = (activities, schedule_id) => ({
  type: ACTIVITIES_BY_SCHEDULE,
  payload: activities,
  schedule_id,
});

const addActivity = (activity) => ({
  type: ADD_ACTIVITY,
  payload: activity,
});

const deleteActivity = (activityId) => ({
  type: DELETE_ACTIVITY,
  activityId,
});

// get activities by scheduleId
export const thunkActivitiesBySchedule = (schedule_id) => async (dispatch) => {
  const response = await fetch(`/api/activities/schedule/${schedule_id}`);
  const data = await response.json();
  if (response.ok) {
    dispatch(activitiesBySchedule(data));
    return data;
  }
  return data;
};

// create new activity
export const thunkNewActivity = (activity) => async (dispatch) => {
  const scheduleId = activity.schedule_id;

  const response = await fetch(`/api/activities/schedule/${scheduleId}/new`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(activity),
  });

  const data = await response.json();
  if (response.ok) {
    dispatch(addActivity(data));
    return data;
  }
  return data;
};

// delete activity
export const thunkDeleteActivity = (activityId) => async (dispatch) => {
  const response = await fetch(`/api/activities/${activityId}`, {
    method: "DELETE",
  });
  const data = await response.json();
  if (response.ok) {
    dispatch(deleteActivity(data));
    return data;
  }
  return data;
};

const initialState = {
  activitiesBySchedule: {},
};

function activityReducer(state = initialState, action) {
  switch (action.type) {
    case ACTIVITIES_BY_SCHEDULE: {
      let newState = {};
      action.payload.forEach((activity) => {
        newState[activity.id] = activity;
      });
      return { ...state, activitiesBySchedule: newState };
    }
    case ADD_ACTIVITY: {
      const activityId = action.payload.id;
      const newState = {};
      if (state.activitiesBySchedule) {
        const newActivitiesBySchedule = {
          ...state.activitiesBySchedule,
          [activityId]: action.payload,
        };
        newState["activitiesBySchedule"] = newActivitiesBySchedule;
      }
      return { ...state, newState };
    }
    case DELETE_ACTIVITY: {
      const newState = { ...state };
      delete newState.activitiesBySchedule[action.activityId];
      return newState;
    }
    default:
      return state;
  }
}

export default activityReducer;
